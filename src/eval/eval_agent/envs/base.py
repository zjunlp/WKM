import json
from abc import ABC, abstractmethod
from typing import Tuple

from eval_agent.utils.datatypes import State


class BaseEnv(ABC):
    def __init__(
        self,
        instruction_ag_path: str,
        instruction_wm_path: str,
        icl_ag_path: str,
        icl_wm_path: str,
        icl_format: str = "first",
        max_steps: int = 10,
        is_icl: bool = True,
        **kwargs,
    ):
        with open(instruction_ag_path) as f:
            self.instruction_ag = f.read()
        with open(instruction_wm_path) as f:
            self.instruction_wm = f.read()
        self.raw_ag_icl = json.load(open(icl_ag_path))
        self.raw_wm_icl = json.load(open(icl_wm_path))
        self.icl_format = icl_format
        self.max_steps = max_steps
        self.is_icl = is_icl


    @abstractmethod
    def step(self, llm_output: str) -> Tuple[str, State]:
        pass

    @abstractmethod
    def reset(self) -> Tuple[str, State]:
        pass
