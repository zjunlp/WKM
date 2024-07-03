import json
import argparse
import os
import getpass
import openai
os.environ['OPENAI_API_BASE'] = "http://localhost:8000/v1"
os.environ['OPENAI_API_KEY'] = "EMPTY"
from langchain_community.document_loaders import TextLoader,JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings

def state_action_build(file_path,output_path):
    with open(file_path,"r") as f:
        data = json.load(f)
        sa_pair = []
        pre_action = "look"
        for d in data:
            pre_action = "look"
            for i in range(2,len(d["conversations"]),2):
                state = d["conversations"][i]["state"]
                action = d["conversations"][i+1]["value"]
                
                action = action.split("Action: ")[1]
                action = action.split('[')[0]
                sa_pair.append({"pre_action":pre_action,"state":state,"action":action})
                pre_action = action
    with open(output_path,"w") as f:
        json.dump(sa_pair,f,indent=4)
        
        
def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["action"] = record.get("action")
    metadata["pre_action"] = record.get("pre_action")
    return metadata



def vector_cache_build(action_pair,vector_cache_path): 
    print("vector cache begin building...")
    embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
    loader = JSONLoader(
        file_path=action_pair,
        jq_schema=".[] ",
        content_key="state",
        metadata_func=metadata_func,
        
        
    )
    documents = loader.load()
    print(len(documents))
    documents

    store = LocalFileStore(vector_cache_path)
    underlying_embeddings = embedding
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
        underlying_embeddings, store, namespace=underlying_embeddings.model
    )
    db = Chroma.from_documents(documents, cached_embedder)   
    print("Success Build")
        

def main(args):
    state_action_build(args.state_file_path,args.state_action_pair_path)
    vector_cache_build(args.state_action_pair_path,args.vector_cache_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--state_file_path", type=str, default="")
    parser.add_argument("--state_action_pair_path", type=str, default="")
    parser.add_argument("--vector_cache_path", type=str, default="")
    args = parser.parse_args()
    main(args)
        