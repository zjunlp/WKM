import re
import json
import logging
from typing import Any, Dict, List, Tuple

from eval_agent.envs import BaseEnv
from eval_agent.tasks import AlfWorldTask
from eval_agent.prompt import prompt_with_icl
from eval_agent.utils.datatypes import State


logger = logging.getLogger("agent_frame")

PROMPT_WITHOUT_ICL_TEMPLATE = """{instruction}

{task}"""

def find_example(game_file,examples):
    for e in examples:
        if e["task"] in game_file:
            return e["example"]
    

def process_ob(ob):
    if ob.startswith('You arrive at loc '):
        ob = ob[ob.find('. ')+2:]
    return ob


class AlfWorldEnv(BaseEnv):
    def __init__(
        self,
        task: AlfWorldTask,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.task: AlfWorldTask = task
        self.env = task.env
        self.state = State()

    def parse_action(self, llm_output: str) -> str:
        llm_output = llm_output.strip()
        pattern = re.compile(r"Action:\s?(.*)", re.DOTALL)
        action = re.findall(pattern, llm_output)[0]
        assert action is not None
        punctuations = [".", "!", "?", ",", ";", ":"]
        while action and action[-1] in punctuations:
            action = action[:-1]
        return action.lower()
    
    def conduct_action(self, action: str):
        observation, reward, done, info = self.env.step([action])
        observation, reward, done = process_ob(observation[0]), info['won'][0], done[0]
        return observation, reward, done
    
    def step(self, llm_ag_output: str) -> Tuple[str, State]:
        self.state.history_ag.append({
            "role": "assistant",
            "content": llm_ag_output
        })
        try:
            action = self.parse_action(llm_ag_output)
            observation, reward, done = self.conduct_action(action)
        except Exception as e:
            # logger.debug(f"Agent failed with error: {e}")
            self.state.success = False
            self.state.finished = False
            self.state.reward=0
            observation = f"Observation: Error Input. Your output must contain Action:..."
            self.state.history_ag.append({
                "role": "user",
                "content": observation
            })
            self.state.history_wm.append({
                "role": "user",
                "content": llm_ag_output+'\n'+observation
            })
            self.state.steps += 1
            if self.state.steps >= self.max_steps:
                self.state.finished = True
                self.state.success = False
                self.state.terminate_reason = "max_steps"
                self.state.reward = 0
            return observation, self.state

        # if observation == "Nothing happens.":
        # #     observation = '''Nothing happens because of the Error input,The available actions are:\n1. go to {recep}\n2. take {obj} from {recep}\n3. put {obj} in/on {recep}\n4. open {recep}\n5. close {recep}\n6. toggle {obj} {recep}\n7. clean {obj} with {recep}\n8. heat {obj} with {recep}\n9. cool {obj} with {recep}\nwhere {obj} and {recep} correspond to objects and receptacles.Please make sure the action is in the correct format and obj you use have been found.Your response should use the following format:Thought: <your thoughts>\nAction: <your next action>'''
        #     observation += "Please check your input format and history action flow, if the task is pick_cool/hear_then_place, you should first pick the object, then cool/heat it, and finally put it in the place."
        observation = f"Observation: {observation}"
        self.state.history_ag.append({
            "role": "user",
            "content": observation,
        })
        self.state.history_wm.append({
            "role": "user",
            "content": llm_ag_output+'\n'+observation
        })

        self.state.steps += 1
        if self.state.steps >= self.max_steps:
            self.state.finished = True
            self.state.success = False
            self.state.terminate_reason = "max_steps"
            self.state.reward = reward

        if done:
            self.state.finished = True
            self.state.success = True
            self.state.terminate_reason = "success"
            self.state.reward = reward

        return observation, self.state

    # def reset(self) -> Tuple[str, State]:
    #     self.state = State()
    #     self.state.error = self.task.game_file
    #     cur_task = self.task.observation
    #     observation, messages = prompt_with_icl(self.instruction, self.raw_icl, cur_task, 1)
    #     if self.icl_format == 'first':
    #         self.state.history.append({
    #             "role": "user",
    #             "content": observation,
    #         })
    #     elif self.icl_format == 'conversation':
    #         self.state.history = messages
    #     return observation, self.state

    def reset(self) -> Tuple[str, State]:
        self.state = State()
        self.state.error = self.task.game_file
        cur_task = self.task.observation
        self.raw_ag_icl = find_example(self.state.error, self.raw_ag_icl)
        self.raw_wm_icl = find_example(self.state.error, self.raw_wm_icl)
        if self.is_icl:  
            observation, ag_messages = prompt_with_icl(self.instruction_ag, [self.raw_ag_icl], cur_task, 1)
            observation, wm_messages = prompt_with_icl(self.instruction_wm, [self.raw_wm_icl], cur_task, 1)
        else:
            ag_messages = []
            wm_messages = []
            
            ag_messages.append({
                "role": "user",
                "content": self.instruction_ag,
            })
            ag_messages.append({
                "role": "assistant",
                "content": "OK"
            })
            ag_messages.append({
                "role": "user",
                "content": cur_task
            })
            # wm_message
            wm_messages.append({
                "role": "user",
                "content": self.instruction_wm,
            })
            wm_messages.append({
                "role": "assistant",
                "content": "OK"
            })
            wm_messages.append({
                "role": "user",
                "content": cur_task
            })
        observation = PROMPT_WITHOUT_ICL_TEMPLATE.format(instruction=self.instruction_ag, task=cur_task)
        if self.icl_format == 'first':
            self.state.history_ag.append({
                "role": "user",
                "content": observation,
            })
        elif self.icl_format == 'conversation':
            self.state.history_ag = ag_messages
            self.state.history_wm = wm_messages
        return observation, self.state
