import torch
from transformers import AutoTokenizer
from eval_agent.utils.documentsearch import DocumentSearch
from math import isclose

# Embed the query and search by vector



legal_action_map ={
    "AlfWorldEnv": ["go","take","clean","use","examine","look","heat","cool","open","close","toggle","put"],
    "WebShopEnv":["search","click"],
    "SciWorldEnv": ['0','1','2','3','4','5','6','7','8','9','look','pick','focus','teleport', 'use', 'move', 'connect', 'wait', 'activate', 'examine', 'deactivate', 'pour', 'mix','open','close', 'read','disconnect'],
}

model_path ={
    "mistral":"",
    "gemma": "",
    "llama-3-8b":""
}

def get_action_gen_prob(model_name,probs,task):
    tokenizer_path =""
    for k,v in model_path.items():
        if k in model_name:
            tokenizer_path = v
            break
    assert tokenizer_path != "" , "Model not found"
    try:
        tokenizer = AutoTokenizer.from_pretrained(
                tokenizer_path,
                use_fast=True,
                trust_remote_code=True,
            )
    except TypeError:
        tokenizer = AutoTokenizer.from_pretrained(
            tokenizer_path, use_fast=False,  trust_remote_code=True
        )
    legal_action = legal_action_map[task]
    action_ids = [ tokenizer(a,add_special_tokens=False).input_ids for a in legal_action]
    if task == "SciWorldEnv":
        for i in range(10):
            action_ids[i] = action_ids[i][1:]
    action_probs = [probs[i[0]] for i in action_ids]
    
    action_probs = torch.tensor(action_probs)
    action_probs = torch.softmax(action_probs,dim=-1)
    return {a:p.item() for a,p in zip(legal_action,action_probs) }


def calculate_first_word_distribution(lst):
    word_count = {}
    total_words = 0

    for item in lst:
        words = item.split()
        if len(words) > 0:
            first_word = words[0]
            word_count[first_word] = word_count.get(first_word, 0) + 1
            total_words += 1

    distribution = {}
    for word, count in word_count.items():
        probability = count / total_words
        distribution[word] = probability

    return distribution



def get_action_know_prob_pre_action(search_engine,summarize,search_by,k,pre_action=None):
    query  = summarize
    # search has inited 
    
    # Search by query
    if search_by == "query":
        query_results = search_engine.search_by_query(query,k)
        if pre_action is not None or pre_action.strip().isdigit() :
            try:
                action  = [q.metadata["action"] for q in query_results if q.metadata["pre_action"].split()[0] == pre_action.split()[0]]
            except:
                print("Error for pre action")
                action = [q.metadata["action"] for q in query_results]
        else:
            action  = [q.metadata["action"] for q in query_results]
    #Search by vector
    else:  
        embedding_vector = search_engine.embedding.embed_query(query)
        vector_results = search_engine.search_by_vector(embedding_vector,k = k)
        if pre_action is not None and not pre_action.strip().isdigit():
            try:
                if '[' in pre_action:
                    pre_action = pre_action.split('[')[0]
                else:
                    pre_action = pre_action.split()[0]
                action = [v.metadata["action"] for v in vector_results if v.metadata["pre_action"].split()[0] == pre_action]
            except:
                print("Error for pre action")
                action = [v.metadata["action"] for v in vector_results]
        else:
            action = [v.metadata["action"] for v in vector_results]
    return calculate_first_word_distribution(action)
    


def get_action_know_prob(search_engine,summarize,search_by,k):

    query  = summarize
    # search has inited 
    
    # Search by query
    if search_by == "query":
        query_results = search_engine.search_by_query(query,k)
        action  = [q.metadata["action"] for q in query_results]
    #Search by vector
    else:  
        embedding_vector = search_engine.embedding.embed_query(query)
        vector_results = search_engine.search_by_vector(embedding_vector,k = k)
        action = [v.metadata["action"] for v in vector_results]
    return calculate_first_word_distribution(action)


def get_next_action(model_name,search_engine,gen_probs,task,llm_wm_output,search_by = "vector",k=10,gen_weight=0.7,pre_action=None):
    action_gen_probs = get_action_gen_prob(model_name,gen_probs,task)
    action_know_probs = get_action_know_prob_pre_action(search_engine,llm_wm_output,search_by,k,pre_action)
    pass
    # if action gen_probs all nan, then use action_know_probs
    action_gen_p = [v for _,v in action_gen_probs.items()]
    if torch.isnan(torch.tensor(action_gen_p)).all().item():
        return action_know_probs
    for k,v in action_gen_probs.items():
        action_gen_probs[k] = action_gen_probs[k]*gen_weight
    for k,v in action_know_probs.items():
        action_gen_probs[k] = action_gen_probs.get(k,0) + (1-gen_weight)*v
    action_gen_probs
    print(action_gen_probs)
    # assert isclose(sum(action_gen_probs.values()),1.0), "Probabilities not sum to 1"
    return action_gen_probs
        