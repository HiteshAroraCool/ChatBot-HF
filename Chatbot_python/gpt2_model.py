from transformers import GPT2Tokenizer, GPT2LMHeadModel
import _pickle

question = "what is botpenguin?"

# Load pre-trained model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

with open("data.pkl", "rb") as f:
    loaded_data = _pickle.load(f)
context = loaded_data.get('context', None)

input_text = question + context


# Tokenize the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate output
output = model.generate(input_ids, max_length=len(input_text), num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)

# Decode the generated output
output_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Print the generated text
print("from context answer my question:", input_text)
print("Generated Output:", output_text)