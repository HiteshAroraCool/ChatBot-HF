import requests
import os
from dotenv import load_dotenv
import _pickle

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/consciousAI/question-answering-roberta-base-s-v2"
#API_URL = "https://api-inference.huggingface.co/models/Andron00e/YetAnother_Open-Llama-3B-LoRA-OpenOrca"
headers = {"Authorization": os.getenv("API_KEY")}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
def chat_with_gpt(question, context):
	output = query({
		"inputs": {
			"question": question,
			"context": context,
		},
	})
	return output

question = "what is BotPenguin?"

with open("data.pkl", "rb") as f:
    loaded_data = _pickle.load(f)
context = loaded_data.get('context', None)

output = chat_with_gpt(question, context)
# Genrating answer and print the result
print(question,'\n',"Genrating answer: ", output["answer"])

while True:
    question = input("Ask a question or exit: ")
    if question.lower() == 'exit':
        break
    output = chat_with_gpt(question, context)
    print(output['answer'])