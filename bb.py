import requests
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from transformers import pipeline

load_dotenv()

question = "what is BotPenguin?"
prompt_template = "With a limit of 100 words, answer the following question: {}"
context = """
BotPenguin is the best AI Chatbot maker platform. Create a Chatbot for WhatsApp, Website, Facebook Messenger, Telegram, WordPress & Shopify with BotPenguin - 100% FREE!
Our chatbot creator helps with lead generation, appointment booking, customer support, marketing automation, WhatsApp & Facebook Automation for businesses.
AI-powered No-Code chatbot maker with live chat plugin & ChatGPT integration.
"""

# Uncomment this section if you want to read context from data.pkl
# with open("data.pkl", "rb") as f:
#     context = pickle.load(f)

# Instantiate PromptTemplate with input_variables
prompt_template = PromptTemplate(input_variables=["question"], template=prompt_template)

# Generate prompt using the template
prompt = prompt_template.generate_prompt(question=question, context=context)

# Use a pipeline as a high-level helper
model_bert = "huggingface-course/bert-finetuned-squad"
model_llama = "codellama/CodeLlama-7b-Python-hf"  # You may use this model later

# Make sure to provide a context string as a list, even if it's just one context
question_answerer = pipeline("question-answering", model=model_bert, context=context)

# Print the result
print(question_answerer(question=prompt))