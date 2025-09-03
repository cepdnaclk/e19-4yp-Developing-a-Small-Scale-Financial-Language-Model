import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


# Point this to your fine-tuned Llama 3 (merged LoRA or full finetune)
MODEL_NAME = os.getenv("LLM_MODEL", "meta-llama/Meta-Llama-3-8B-Instruct")
DTYPE = torch.float16 if torch.cuda.is_available() else torch.float32


_tokenizer = None
_model = None


def load_llm():
global _tokenizer, _model
if _model is None:
_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
_model = AutoModelForCausalLM.from_pretrained(
MODEL_NAME,
torch_dtype=DTYPE,
device_map="auto"
)
return _tokenizer, _model


@torch.inference_mode()
def generate(prompt: str, max_new_tokens: int = 512) -> str:
tok, model = load_llm()
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.2, top_p=0.9)
return tok.decode(out[0], skip_special_tokens=True)
