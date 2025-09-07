"""
QLoRA fine-tuning script for financial LLaMA-3.
"""

import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
from trl import SFTTrainer

MODEL_NAME = os.getenv("LLM_MODEL", "meta-llama/Meta-Llama-3-8B-Instruct")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./qlora-financial-llama")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

# 4-bit quantization config for QLoRA
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

# Load base model
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto",
)

# Define LoRA config
lora_config = LoraConfig(
    r=64,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

# Apply LoRA
model = get_peft_model(model, lora_config)

# Load dataset (expects JSONL or pre-split HuggingFace dataset)
dataset_path = os.getenv("DATASET_PATH", "financial_data.json")
dataset = load_dataset("json", data_files={"train": dataset_path})

# Fine-tune with TRL’s SFTTrainer
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset["train"],
    peft_config=lora_config,
    max_seq_length=512,
    packing=True,
    output_dir=OUTPUT_DIR,
)

trainer.train()
trainer.model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
