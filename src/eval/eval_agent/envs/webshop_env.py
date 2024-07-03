import re
import json
import logging
from typing import Tuple

from eval_agent.envs import BaseEnv
from eval_agent.tasks import WebShopTask
from eval_agent.prompt import prompt_with_icl
from eval_agent.utils.datatypes import State
from webshop.web_agent_site.envs import WebAgentTextEnv


logger = logging.getLogger("agent_frame")
PROMPT_WITHOUT_ICL_TEMPLATE = """{instruction}

{task}"""

class WebShopEnv(BaseEnv):
    def __init__(
        self,
        task: WebShopTask,
        env: WebAgentTextEnv,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.task: WebShopTask = task
        self.session_id = self.task.session_id
        self.session = {}
        self.env = env
        
        self.state = State()
    
    def parse_action(self, llm_output: str) -> str:
        llm_output = llm_output.strip()
        pattern = re.compile(r"Action: (.*)", re.DOTALL)
        action = re.findall(pattern, llm_output)[0]
        assert action is not None
        punctuations = [".", "!", "?", ",", ";", ":"]
        while action and action[-1] in punctuations:
            action = action[:-1]
        return action
    
    def step(self, llm_ag_output: str) -> Tuple[str, State]:
        self.state.history_ag.append({
            "role": "assistant",
            "content": llm_ag_output
        })
        try:
            action = self.parse_action(llm_ag_output)
        except:
            observation = f"Observation: Invalid format. The input must contains 'Action: '"
            self.state.history_ag.append({
                "role": "user",
                "content": observation,
            })
            self.state.history_wm.append({
                "role": "user",
                "content": llm_ag_output+'\n'+observation
            })
            self.state.steps += 1
            self.state.reward = 0
            if self.state.steps >= self.max_steps:
                self.state.finished = True
                self.state.success = False
                self.state.terminate_reason = "max_steps"
                self.state.reward = 0
            return observation, self.state
        try:
            observation, reward, done, info = self.env.step(action=action)
            observation = f"Observation:\n{observation}"
            # available_actions = self.env.get_available_actions()
            # observation = f"Observation:\n{observation}\n\nAvailable Actions:\n{available_actions}"
        except AssertionError:
            observation = 'Observation: Invalid action!'
            done = False

        self.state.history_ag.append({
            "role": "user",
            "content": f"{observation}",
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

        if done:
            self.state.finished = True
            self.state.success = True
            self.state.terminate_reason = "success"
            self.state.reward = reward

        return observation, self.state
    
    def reset(self) -> Tuple[str, State]:
        self.state = State()
        self.env.reset(self.session_id)
        cur_task = self.env.observation
        self.raw_ag_icl = self.raw_ag_icl
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
