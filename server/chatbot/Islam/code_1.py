import os
import openai
from key1 import KEY
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext

openai.api_key = KEY
os.environ["OPENAI_API_KEY"] = KEY

documents = SimpleDirectoryReader('docs').load_data()
index = VectorStoreIndex.from_documents(documents)

storage_context = StorageContext.from_defaults()
index.storage_context.persist()
print("done")