import requests
from dotenv import load_dotenv
from transformers import pipeline
import _pickle

load_dotenv()

question = "what is BotPenguin?"
prompt = "answer the following question: " + question


with open("data.pkl", "rb") as f:
    context, label = _pickle.load(f)

#Choose model
#short answer, high score
#model = "atharvamundada99/bert-large-question-answering-finetuned-legal"

#the best AI Chatbot maker platform 0.4783157706260681
model = "consciousAI/question-answering-roberta-base-s-v2" 

# context length issue
"""# Load model directly
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model_deepset = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
inpu1 = tokenizer(prompt, context, return_tensors='pt')
print(model_deepset(**inpu1))"""

# Cannot allocate memory (12) error
#model_llama = "codellama/CodeLlama-7b-Python-hf"  

#hugging face pipeline
# Use a pipeline as a high-level helper
question_answerer = pipeline("question-answering", model=model)

# Genrating answer and print the result
print(question,'\n',"Genrating answer: ")
anw_dict = question_answerer(question=prompt, context=context)
print(anw_dict['answer'], "; Score: ", anw_dict["score"])