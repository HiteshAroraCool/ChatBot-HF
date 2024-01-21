from transformers import pipeline
import _pickle

question = "what is BotPenguin?"

with open("data.pkl", "rb") as f:
    loaded_data = _pickle.load(f)
context = loaded_data.get('context', None)
label = loaded_data.get('label', None)

# Model
# the best AI Chatbot maker platform 0.4783157706260681
model = "consciousAI/question-answering-roberta-base-s-v2" 
# Cannot allocate memory (12) error
# model_llama = "codellama/CodeLlama-7b-Python-hf"  

# Hugging face pipeline
# Use a pipeline as a high-level helper
question_answerer = pipeline("question-answering", model=model)

# Generating answer and print the result
print(question, '\n', "Generating answer: ")
anw_dict = question_answerer(question=question.upper(), context=context)
print(anw_dict['answer'], "; Score: ", anw_dict["score"])