import requests
import os
from dotenv import load_dotenv
import _pickle
import time
load_dotenv()


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
def chat_with_gpt(question, context):
    try:
        output = query({
                "inputs": {
                    "question": question,
                    "context": context,
                },
            })
    except Exception as e:
         print(output, e)

    if 'estimated_time' in output:
        print(f"Model loading, {output['estimated_time']} sec", output)
        time.sleep(output['estimated_time'])
        print('Model Running')
        output = query({
            "inputs": {
                "question": question,
                "context": context,
            },
        })
    return output



API_URL = "https://api-inference.huggingface.co/models/consciousAI/question-answering-roberta-base-s-v2"

headers = {"Authorization": os.getenv("API_KEY")}

question = "what is BotPenguin?"

with open("data.pkl", "rb") as f:
    loaded_data = _pickle.load(f)
context = loaded_data.get('context', None)

output = chat_with_gpt(question, context)
#print(output)
# Genrating answer and print the result
print(question,'\n',"Genrating answer: ", output["answer"])

while True:
    question = input("Ask a question or exit: ")
    if question.lower() == 'exit':
        break
    output = chat_with_gpt(question, context)
    print(f"Genrating answer: {output['answer']}\n\n",end='')