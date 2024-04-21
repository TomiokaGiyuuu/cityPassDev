from llama_index.core import StorageContext, load_index_from_storage

from key1 import KEY 
import os
import openai

os.environ['OPENAI_API_KEY'] = KEY 

storage_context = StorageContext.from_defaults(persist_dir='./storage')

index = load_index_from_storage(storage_context)


def generate_response(prompt):
	query_engin = index.as_query_engine() 

	question = prompt
	response = query_engin.query(question)
	print ("\n", response)
	# return str(response)


generate_response('Здравствуйте')

