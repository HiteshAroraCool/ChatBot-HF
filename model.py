import requests
from dotenv import load_dotenv
from transformers import pipeline
import _pickle

load_dotenv()

question = "what is BotPenguin?"
prompt = "answer the following question: " + question
context = """
BotPenguin is the best AI Chatbot maker platform. Create a Chatbot for WhatsApp, Website, Facebook Messenger, Telegram, WordPress & Shopify with BotPenguin - 100% FREE!
Our chatbot creator helps with lead generation, appointment booking, customer support, marketing automation, WhatsApp & Facebook Automation for businesses.
AI-powered No-Code chatbot maker with live chat plugin & ChatGPT integration.
"""

with open("data.pkl", "rb") as f:
    context, label = _pickle.load(f)

#Choose model
#short answer, high score
#model = "atharvamundada99/bert-large-question-answering-finetuned-legal"

#the best AI Chatbot maker platform 0.4783157706260681
model = "consciousAI/question-answering-roberta-base-s-v2" 

# Cannot allocate memory (12) error
#model_llama = "codellama/CodeLlama-7b-Python-hf"  

#hugging face pipeline
# Use a pipeline as a high-level helper
question_answerer = pipeline("question-answering", model=model)

# Genrating answer and print the result
print(question,'\n',"Genrating answer: ")
anw_dict = question_answerer(question=prompt, context=context)
print(anw_dict['answer'], "; Score: ", anw_dict["score"])