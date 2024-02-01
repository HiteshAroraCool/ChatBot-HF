from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig, AutoModelForCausalLM, TextStreamer, Trainer, TrainingArguments
import _pickle
import transformers


model_name = 'gpt2'

with open("data.pkl", "rb") as f:
    loaded_data = _pickle.load(f)
context = loaded_data.get('context', None)

prompt = "'question': 'What is botpenguin?'+'Answer':'BotPenguin is the best AI Chatbot maker platform Create a Chatbot for WhatsApp Website Facebook Messenger Telegram WordPress Shopify with BotPenguin'".strip()
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot talking to a client providing answer to question based on context",
    },
    {"role": "user", "content": "What is botpenguin?"},
]

tokenizer = AutoTokenizer.from_pretrained(model_name, truncation=True, padding=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

model_inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to("cuda")
input_length = model_inputs.shape[1]
generated_ids = model.generate(model_inputs, do_sample=True, max_new_tokens=20)
print(tokenizer.batch_decode(generated_ids[:, input_length:], skip_special_tokens=True)[0])

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=2,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    fp16=True,
    save_total_limit=3,
    logging_steps=1,
    optim="paged_adamw_8bit",
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,

)

trainer = Trainer(
    model=model_name,
    training_args=training_args,
    train_dataset=context,
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False)
)

trainer.train()