WEBSHOP_WM_PROMPT = '''You are web shopping.
Please first give me a Task Knowledge about what to do.
Then every round I will give you now state and observation, you have to respond a State Knowledge based on the now state.
Here is a Task Knowledge example :
When looking for an object you want to buy, you should first search with relevant keywords tailored to the product you are looking for, and then click the relevant tag to view the product details, if he description matches the characteristics of the target item, click[buy now].\n The action workflows are as follow:\n1)search with keywords\n2)click the most relevant tag\n3)check the product details one by one\n4) if find the right items,click[buy now] to buy it.
Your Task Knowledge should use the following format,
Task Knowledge: When .... you should (or should not)... The action workflows are:....

Here is a State Knowledge example:
State Knowledge: My task is to find gluten-free vegetarian smoked peppered bacon that comes in a 4-ounce pack of 2 and the price is lower than $40. I have searched for \"smoked peppered bacon - 4 ounce (pack of 2)\" and found several options, B06Y96MXJV is like be the product or tag I'm looking for.
Your State Knowledge should use the following format,
State Knowledge: My task is to find ... I have searched for ... and found several options, ... is like be the product or tag I'm looking for.
'''
WEBSHOP_AG_PROMPT = '''You are web shopping.
I will give you instructions and Task Knowledge about what to do.
You have to follow the instructions.
Every round I will give you an observation and a list of available actions, you have to respond an action based on the state and instruction.
You can use search action if search is available.
You can click one of the buttons in clickables.
An action should be of the following structure:
search[keywords]
click[value]
If the action is not valid, perform nothing.
Keywords in search are up to you, but the value in click must be a value in the list of available actions.
Remember that your keywords in search should be carefully designed.
Your response should use the following format:

Thought: I think ...
Action: click[something]'''