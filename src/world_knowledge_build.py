import json
import argparse
from utils.llms import llm
from tqdm import tqdm
from prompts.knowledge_template import TASK_KNOWLEDGE, STATE_KNOWLEDGE,ALFWORLD_EXAMPLES,WEBSHOP_EXAMPLES,SCIWORLD_EXAMPLES
task_knowledege_format = TASK_KNOWLEDGE
state_knowledge_format = STATE_KNOWLEDGE


alfworld_example = ALFWORLD_EXAMPLES 
webshop_example = WEBSHOP_EXAMPLES
sciworld_example = SCIWORLD_EXAMPLES


def model (prompt, stop='',model="mistral", temperature=0.5, max_tokens=512):
    return llm(
        stop = stop,
        model = model,
        prompt = prompt,
        temperature = temperature,
        max_tokens = max_tokens
    )

def get_alfworld_example(data):
    for k,v in alfworld_example.items():
        if k in data["game_file"]:
            return v
    
def get_sciworld_example(data):
    id = data["id"]
    task = id.split("_")[0]
    return sciworld_example[task]
def get_trajectory(data):
    tra_rejected = ""
    tra_chosen = ""
    for conv_r in data["rejected"]["conversations"]:
        if conv_r["value"].startswith("Observation:"):
            tra_rejected += conv_r["value"][:1000]+'\n'
        else:
            tra_rejected += conv_r["value"]+'\n'
    for conv_c in data["chosen"]["conversations"]:
        if conv_c["value"].startswith("Observation:"):
            tra_chosen += conv_c["value"][:1000]+'\n'
        else:
            tra_chosen += conv_c["value"]+'\n'
    return tra_rejected,tra_chosen


def task_knowledge_gen(data,output_path,model_name,task):
    guidlines = []
    with tqdm(total=len(data), desc="Processing data") as pbar:
        for d in data:
            tra_r,tra_c= get_trajectory(d) 
            if task == "alfworld":
                example = get_alfworld_example(d["chosen"])
            elif task == "webshop":
                example = webshop_example
            elif task == "sciworld":
                example = get_sciworld_example(d["chosen"])
            input  = task_knowledege_format["Instruction"]+task_knowledege_format['Input'].format(Success_T=tra_c,Failed_T=tra_r,Example=example) 
            try:
                model_output = model(prompt = input,model=model_name)
            except :
                print(f"error{input}")
            d["task_knowledege"] = model_output
            guidlines.append(d)
            print(f"input\n{input}\n\n\noutput:\n{model_output}\n\n\n")
            pbar.update(1)
            with open(f"{output_path}", 'w') as f:
                json.dump(guidlines, f, indent=4)
                
def state_knowledge_sum(data, output_path,model_name,task):
    with tqdm(total=len(data), desc="Processing data") as pbar:
        state_knowledge_data = []
        for d in data:
            trajectory = ""
            convs = []
            for conv in d["chosen"]["conversations"]:
                if conv["value"].startswith("Observation:"):
                    trajectory += conv["value"]+'\n'
                else:
                    trajectory += conv["value"]+'\n'
                if conv['from'] == "human" :
                    input  = state_knowledge_format["Instruction"]+'\n'+state_knowledge_format['Example'][task]+'\n'+state_knowledge_format['Input'].format(Trajectory = trajectory)
                    model_output = model(prompt = input,stop='\n',model=model_name,max_tokens=128)
                    print("OUTPUT: ",model_output)
                    conv['state_knowledge'] = model_output.strip()
                    trajectory += conv["state_knowledge"]+'\n'
                convs.append(conv)
            d["chosen"]["conversations"] = convs
            state_knowledge_data.append(d["chosen"])
            pbar.update(1)
            with open(f"{output_path}", 'w') as f:
                json.dump(state_knowledge_data, f, indent=4)         
                
                
def main(args):
    # read jsonlines
    with open(args.dataset_path, 'r') as f:
        data = json.load(f)
        print(f"all process {len(data)} datas")
        model_name = args.model_name
        output_path = args.output_path
        if args.gen =="task_knowledge":
            task_knowledge_gen(data,output_path,model_name,args.task)
        elif args.gen =="state_knowledge":
            state_knowledge_sum(data,output_path,model_name,args.task)


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, default="")
    parser.add_argument("--task", type=str, default="sciworld")
    parser.add_argument("--gen", type=str, default="task_knowledege")
    parser.add_argument("--model_name",type=str,default="mistral")
    parser.add_argument("--output_path", type=str, default="")
    args = parser.parse_args()
    main(args)

