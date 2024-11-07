import json 
import json
import argparse
from prompts.alfworld_prompt import ALFWORLD_WM_SYSTEM_PROMPT,ALFWORLD_AG_SYSTEM_PROMPT
from prompts.webshop_prompt import WEBSHOP_WM_PROMPT,WEBSHOP_AG_PROMPT
from prompts.sciworld_prompt import SCIWORLD_WM_PROMPT,SCIWORLD_AG_PROMPT
prompts= {
    "alfworld":{
        "wm":ALFWORLD_WM_SYSTEM_PROMPT,
        "agent":ALFWORLD_AG_SYSTEM_PROMPT
    },
    "webshop":{
        "wm":WEBSHOP_WM_PROMPT,
        "agent":WEBSHOP_AG_PROMPT
    },
    "sciworld":{
        "wm":SCIWORLD_WM_PROMPT,
        "agent":SCIWORLD_AG_PROMPT
    }   
        
}

def guideline_filter(guideline):
    if "\n" in guideline:
        guideline = guideline.split("\n")
    for g in guideline:
        if g.startswith("Guideline"):
            return g.strip()
    return guideline[0].replace("Reasoning","Guideline")

def find_icl_example(game_file,examples):
    for e in examples:
        if e["task"] in game_file:
            return e["example"]
    print([e["task"] for e in examples],game_file)


def process_wm(file_path,output_path):
    with open(file_path,"r") as f:
        data = json.load(f)
        new_turns = []
        for d in data :
            # example = find_icl_example(d["game_file"],examples)
            convs = d["conversations"]
            system_prompt = convs[0]["value"].strip()

            new_convs = []
            new_convs.append({"from":"human","value":convs[0]["value"]})
            new_convs.append({"from":"gpt","value":convs[1]["value"]})
            # new_convs.extend(example)
            convs = convs[2:]
            assert len(convs)%2 == 0
            pre_action = ""
            for i in range(0,len(convs)-1,2):
                human_conv = (pre_action+'\n'+convs[i]["value"]).strip()
                gpt_conv  = (convs[i]["state_knowledge"]).strip()
                if i ==0:
                    gpt_conv = d["task_knowledge"]
                pre_action = convs[i+1]["value"]
                new_convs.append({"from":"human","value":human_conv})
                new_convs.append({"from":"gpt","value":gpt_conv})
            new_turns.append({"conversations":new_convs})
    return new_turns




def process_ag(file_path,output_path):
    with open(file_path,"r") as f:
        data = json.load(f)
        new_turns = []
        for d in data :
            convs = d["conversations"]
            system_prompt = convs[0]["value"].strip()
            assert len(convs)%2 == 0
            new_convs = []
            new_convs.append({"from":"human","value":convs[0]["value"]})
            new_convs.append({"from":"gpt","value":convs[1]["value"]})
            pre_action = ""
            for i in range(2,len(convs)-1,2):
                human_conv = convs[i]["value"]+'\n'
                if i ==2 :
                    human_conv += d["task_knowledge"]
                else :
                    # human_conv += convs[i]["state_knowledge"]
                    None
                human_conv = human_conv.strip()
                gpt_conv  = convs[i+1]["value"].strip()
                new_convs.append({"from":"human","value":human_conv})
                new_convs.append({"from":"gpt","value":gpt_conv})
            new_turns.append({"conversations":new_convs})
    return new_turns

def main(args):
    mode = args.mode
    task = args.task
    prompt = prompts[task][mode]
    file_path = args.file_path
    output_path = args.output_path
    data = []
    if mode == "world_model":
        data = process_wm(file_path,output_path)
        
    else:
        data = process_ag(file_path,output_path)
    for d in data:
        d["conversations"][0]["value"] = prompt
        
    print(len(data))
    
    with open(output_path,"w") as f:
        json.dump(data,f,indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, default="alfworld")
    parser.add_argument("--file_path", type=str, default="")
    parser.add_argument("--mode", type=str, default="agent_model")
    parser.add_argument("--output_path", type=str, default="output.json")
    args = parser.parse_args()
    main(args)
        
