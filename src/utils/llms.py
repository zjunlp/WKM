from langchain_openai import ChatOpenAI
import os
os.environ['OPENAI_API_KEY'] = "EMPTY"
os.environ['OPENAI_API_BASE'] = "http://localhost:8000/v1"

def llm(model,prompt,stop='',temperature=0.1,max_tokens=128):
    chat = ChatOpenAI(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens)  
    return chat.invoke(prompt, stop=stop).content

