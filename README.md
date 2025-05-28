# 📈 Developing a Small-Scale Financial Language Model

This project focuses on building a **Small Language Model (SLM)** to assist financial data analysis within LEARN. Unlike large language models, this resource-efficient SLM processes financial statements, audit reports, and spreadsheets securely, supporting accurate and regulation-compliant decision-making.

## 📝 Abstract

This study develops a Small Language Model (SLM) to process financial data at LEARN, enhancing decision-making with efficiency and accuracy. Trained on five years of financial statements, audit reports, and spreadsheets, the model leverages:

- **Quantization, pruning, and knowledge distillation**
- **Retrieval-Augmented Generation (RAG)** to reduce hallucination
- **QLoRA** for efficient fine-tuning
- **Secure in-house deployment** on LEARN’s servers

---

## 📚 Related Works

- FinGPT: Open-source LLMs for quantitative finance
- FinancialBERT: Domain-specific transformers for financial NLP
- OpenELM and TinyLLaMA: Compact transformer models
- RAG pipelines and hallucination prevention techniques

---

## ⚙️ Methodology

<img src="https://raw.githubusercontent.com/cepdnaclk/e19-4yp-Developing-a-Small-Scale-Financial-Language-Model/main/docs/images/im.png" alt="Methodology Flow Diagram" width="600"/>

### Key Steps

- 📥 **Data Collection** - Audited financial reports, balance sheets, internal spreadsheets

- 🧹 **Preprocessing** - Tokenization, normalization, and formatting for model ingestion

- 🧠 **Model Selection** - Choose and experiment with SLMs: TinyLLaMA, FinGPT, OpenELM

- 🛠️ **Fine-Tuning with QLoRA** - Apply quantization-aware low-rank adaptation

- ⚙️ **Optimization** - Apply pruning, quantization, and distillation for efficiency

- 📚 **RAG Integration** - Connect to local knowledge base for hallucination control

- 🧪 **Evaluation** - Use BLEU, ROUGE, MAE, hallucination score, and latency metrics

- 🚀 **Deployment**  - Secure REST API hosted on LEARN internal servers

## 📄 Publications

1. [Literature Review Paper](docs/publications/Literature_Review_Paper.pdf)
2. [Project Proposal](docs/publications/Project_Proposal.pdf)

