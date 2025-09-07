
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"
LORA_ADAPTER_DIR = "./qlora-financial-llama"
MERGED_OUTPUT = "./merged-llama-financial"

# Load base + LoRA adapter
base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL, device_map="auto")
model = PeftModel.from_pretrained(base_model, LORA_ADAPTER_DIR)

# Merge weights
model = model.merge_and_unload()

# Save merged model
model.save_pretrained(MERGED_OUTPUT)
AutoTokenizer.from_pretrained(BASE_MODEL).save_pretrained(MERGED_OUTPUT)

print(f" Merged model saved at {MERGED_OUTPUT}")
