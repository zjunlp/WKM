# Agent Planning with World Knowledge Model

This repository is the official implementation of Agent Planning with World Knowledge Model. 

## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

## World Knowlegedge Build

To build the task knowledge
```sh
python world_knowledge_build.py \
    --dataset_path your/rejected and chosen/data/pair \
    --task your/task \
    --gen task_knowledge \
    --model_name your/model/name \
    --output_path your/output/path
```

To build the state knowledge
```sh
python world_knowledge_build.py \
    --dataset_path your/rejected and chosen/data/pair \
    --task your/task \
    --gen state_knowledge \
    --model_name your/model/name \
    --output_path your/output/path
```

After your get task_knowledge and state_knowledge, process the data to train
```
python train_data_process.py \
    --task alfworld \
    --file_path your/path \
    --mode model_type
    --output_path your/output/path
```

And use the state knowledege train data to build state knowledge base
```
python state_base_build.py \
    --state_file_path your/state/knowledge/path \
    --state_action_pair_path path/to/store/state_action/pair \
    --vector_cache_path path/to/store/vector/cache
```
## Train Agent model and World knowledge model
Use LLama-Factory to train the agent model and world model 
```sh
CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch \
    --config_file ./examples/accelerate/single_config.yaml \
    src/train_bash.py \
    --ddp_timeout 180000000 \
    --stage sft \
    --do_train \
    --model_name_or_path /base/model/path \
    --dataset_dir ./data \
    --dataset train_data_for_agent \
    --template model_template \
    --finetuning_type lora \
    --lora_target q_proj,v_proj \
    --output_dir ../lora/peft_model_name \
    --overwrite_cache \
    --per_device_train_batch_size 4\
    --gradient_accumulation_steps 2 \
    --lr_scheduler_type cosine \
    --logging_steps 1 \
    --save_steps 1000 \
    --learning_rate 1e-4 \
    --num_train_epochs 3 \
    --plot_loss \
    --fp16 \
    --cutoff_len 2048 \
    --save_safetensors False \
    --overwrite_output_dir \
    --train_on_prompt False
```


## Evaluation

To evaluate the task, you should first lanuch a local API server with fastchat.
```sh
cd .src/eval
# agent_model
python -u -m fastchat.serve.model_worker \
    --model-path /path/peft/agent_model \
    --port 21020 \ 
    --worker-address http://localhost:21020 \
    --max-gpu-memory 31GiB \
    --dtype float16
# world_knowledge_model
python -u -m fastchat.serve.model_worker \
    --model-path /path/peft/world_model \
    --port 21021 \ 
    --worker-address http://localhost:21021 \
    --max-gpu-memory 31GiB \
    --dtype float16
```

Evaluate the task
```sh
python -m eval_agent.eto_multi_main_probs \
    --agent_config fastchat \
    --agent_model_name agent_model \
    --world_model_name world_model \
    --exp_config alfworld \
    --exp_name eval \
    --split test
```
