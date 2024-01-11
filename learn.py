from datasets import load_dataset
from sklearn.model_selection import train_test_split
from transformers import pipeline, AutoModelForQuestionAnswering, TrainingArguments, Trainer

model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased")
question_answer = pipeline("question-answering")

squad = load_dataset("squad", split="train[:5000]")
squad = train_test_split(test_size=0.2)
print(squad["train"][0])