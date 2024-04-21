import os
import openai
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext

openai.api_key = "sk-proj-etcQQ3Du5bZqjQgrKNRWT3BlbkFJJT5z49XtxGsjENFZTCJ1"
os.environ["OPENAI_API_KEY"] = "sk-proj-etcQQ3Du5bZqjQgrKNRWT3BlbkFJJT5z49XtxGsjENFZTCJ1"

documents = SimpleDirectoryReader('docs').load_data()
index = VectorStoreIndex.from_documents(documents)

storage_context = StorageContext.from_defaults()
index.storage_context.persist()
print("done")