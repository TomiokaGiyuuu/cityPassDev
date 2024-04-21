from llama_index.core import StorageContext, load_index_from_storage

# from key1 import KEY
import os
import openai

os.environ['OPENAI_API_KEY'] = "sk-proj-etcQQ3Du5bZqjQgrKNRWT3BlbkFJJT5z49XtxGsjENFZTCJ1"

storage_context = StorageContext.from_defaults(persist_dir='D:\AITU\Hakaton\server\chatbot\Islam\storage')

index = load_index_from_storage(storage_context)


def generate_response(prompt):
	query_engin = index.as_query_engine() 

	question = prompt
	response = query_engin.query(question)
	# print ("\n", response)
	return str(response)

generate_response('Про что данный текст?')

