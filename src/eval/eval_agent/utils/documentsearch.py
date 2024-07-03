import os
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings
def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["action"] = record.get("action")
    metadata["pre_action"] = record.get("pre_action")
    return metadata
class DocumentSearch:
    def __init__(self, file_path,env, model="text-embedding-ada-002"):
        os.environ['OPENAI_API_BASE'] = "http://localhost:8000/v1"
        os.environ['OPENAI_API_KEY'] = "EMPTY"
        
        self.loader = JSONLoader(file_path=file_path, jq_schema=".[]",content_key="state",metadata_func=metadata_func)
        self.embedding = OpenAIEmbeddings(model=model)
        self.db = None
        if env =="AlfWorldEnv": 
            self.store = LocalFileStore("./vector_cache/alfworld_asa_cache")
        elif env =="WebShopEnv":
            self.store = LocalFileStore("./vector_cache/mistral_webshop")
        elif env == "SciWorldEnv":
            self.store = LocalFileStore("./vector_cache/mistral_sciworld")
            
        
    
    def load_documents(self):
        documents = self.loader.load()
        # documents = documents[:100]
        cached_embedder = CacheBackedEmbeddings.from_bytes_store(
        self.embedding, 
        self.store, 
        namespace=self.embedding.model
        )
        self.db = Chroma.from_documents(documents, cached_embedder)
    
    def search_by_query(self, query,k=1):
        if self.db is None:
            raise ValueError("No documents loaded. Call load_documents() first.")
        
        docs = self.db.similarity_search(query,k=1)
        return docs
    
    def search_by_vector(self, embedding_vector,k=1):
        if self.db is None:
            raise ValueError("No documents loaded. Call load_documents() first.")
        
        docs = self.db.similarity_search_by_vector(embedding_vector,k)
        return docs

