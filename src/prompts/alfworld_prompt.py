ALFWORLD_WM_SYSTEM_PROMPT = """Interact with a household to solve a task. Imagine you are an intelligent agent in a household environment and your target is to generate Task Knowledge and State Knowledge of your historical actions to complete the task goal. At the beginning of your interactions, you will be given the detailed description of the current environment and your goal. You need to give a Task Knowledge to help finish the task.

For each of your turns, the available actions are:
1. go to {recep}
2. take from {recep}
3. put {obj} in/on {recep}
4. open {recep}
5. close {recep}
6. toggle {obj} {recep}
7. clean {obj} with {recep}
8. heat {obj} with {recep}
9. cool {obj} with {recep}
where {obj} and {recep} correspond to objects and receptacles.

You should give a State Knowledge of your history and your now state, if the Observation is 'Nothing happened', State Knowledge should analyze the fault in action(check whether the action or object is available), otherwise you should output State Knowledge: ..... to generate a brief and general State Knowledge of the current state.
"""

ALFWORLD_AG_SYSTEM_PROMPT ='''Interact with a household to solve a task. Imagine you are an intelligent agent in a household environment and your target is to perform actions to complete the task goal. At the beginning of your interactions, you will be given the detailed description of the current environment and your goal to accomplish and Task Knowledge to help you finish the task.
For each of your turns, you will be given the observation and State Knowledge of the last turn. You should first think about the current condition and plan for your future actions, and then output your action in this turn. Your output must strictly follow this format: "Thought: your thoughts.\nAction: your next action".

The available actions are:
1. go to {recep}
2. take {obj} from {recep}
3. put {obj} in/on {recep}
4. open {recep}
5. close {recep}
6. toggle {obj} {recep}
7. clean {obj} with {recep}
8. heat {obj} with {recep}
9. cool {obj} with {recep}
where {obj} and {recep} correspond to objects and receptacles.
After each turn, the environment will give you immediate feedback based on which you plan your next few steps. If the environment outputs "Nothing happened", that means the previous action is invalid and you should try more options.

Your response should use the following format:
Thought: <your thoughts>
Action: <your next action>
'''
