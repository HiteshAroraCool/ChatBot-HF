# https://huggingface.co/docs/transformers/main/en/generation_strategies#text-generation-strategies

#The process of selecting output tokens to generate text is known as decoding.
#max_new_tokens: the maximum number of tokens to generate.

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig, AutoModelForCausalLM, TextStreamer
import _pickle
import os
from dotenv import load_dotenv


load_dotenv()

with open("data.pkl", "rb") as f:
    loaded_data = _pickle.load(f)
context = loaded_data.get('context', None)

#context = 'BotPenguin is the best AI Chatbot maker platform. Create a Chatbot for WhatsApp, Website, Facebook Messenger, Telegram, WordPress & Shopify with BotPenguin - 100% FREE! Our chatbot creator helps with lead generation, appointment booking, customer support, marketing automation, WhatsApp & Facebook Automation for businesses. AI-powered No-Code chatbot maker with live chat plugin & ChatGPT integration.'
question = 'what is botpenguin?'
input_pr = {
            "prompt": 'You are a question-answer model. from context answer the fellowing question',
			"question": question,
			"context": context
	}
#input_pr = "You are a sale person. answer the question to a client:" + question + context

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2", token=os.getenv("API_KEY"))

translation_generation_config = GenerationConfig(
    num_beams=1,
    decoder_start_token_id=0,
    eos_token_id=model.config.eos_token_id,
    pad_token=model.config.eos_token_id,
    max_new_tokens=20
)

# Tip: add `push_to_hub=True` to push to the Hub
translation_generation_config.save_pretrained("/tmp", "translation_generation_config.json")

# You could then use the named generation config file to parameterize generation
generation_config = GenerationConfig.from_pretrained("/tmp", "translation_generation_config.json")
inputs = tokenizer(input_pr, return_tensors="pt")
streamer = TextStreamer(tokenizer)
outputs = model.generate(**inputs, streamer=streamer, generation_config=generation_config)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))