---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: https://github.com/cepdnaclk/e19-4yp-Developing-a-Small-Scale-Financial-Language-Model
title: 
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Developing a Small-Scale Financial Language Model

#### Team

- e19131, Kasuni Hansachapa, [email](mailto:e19131@eng.pdn.ac.lk)

#### Supervisors

- Dr. Asitha Bandaranayake, [email](mailto:asithab@eng.pdn.ac.lk)
- Prof. Roshan G. Ragel, [email](mailto:roshanr@eng.pdn.ac.lk)

#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Publications](#publications)
8. [Links](#links)

---

<!-- 
DELETE THIS SAMPLE before publishing to GitHub Pages !!!
This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/)
![Sample Image](./images/sample.png) 
-->


## Abstract
This study develops a Small Language Model (SLM) to process financial data at LEARN, enhancing decision-making with efficiency and accuracy. Trained on five years of financial statements,audit reports and spreadsheets, the model leverages quantization, pruning, knowledge distillation, and retrieval-augmented generation (RAG). QLoRA optimizes performance, while hallucination reduction ensures reliability. The system, hosted on LEARN’s servers for security, processes structured and unstructured financial data to provide accurate insights. This research highlights SLMs as a secure, regulatory-compliant alternative to LLMs for financial analysis.

## Related works
Large Language Models (LLMs) have revolutionized Natural Language Processing (NLP) with their ability to generate human-like text, enabling applications in code writing, math problem-solving, dialogue, and reasoning. In finance, models like BloombergGPT support automated decision-making, risk assessment, fraud prevention, and forecasting. However, their high computational cost and risk of generating incorrect outputs pose challenges.

Small Language Models (SLMs) offer a resource-efficient alternative with domain-specific accuracy. Techniques like quantization, pruning, and knowledge distillation allow SLMs to match LLM performance with lower computational demands. Fine-tuned on financial documents using QLoRA and enhanced with RAG for hallucination control, SLMs ensure high precision—critical for financial applications. As AI adoption in finance grows, regulatory frameworks and ethical standards continue to evolve.
<table border="1">
  <tr>
    <th>Feature</th>
    <th>SLM</th>
    <th>LLM</th>
  </tr>
  <tr>
    <td><strong>Size & Complexity</strong></td>
    <td>Smaller in size, with fewer parameters</td>
    <td>Massive in size, billions of parameters</td>
  </tr>
  <tr>
    <td><strong>Computational Requirements</strong></td>
    <td>Low computational power; optimized for efficiency</td>
    <td>Requires high-end GPUs/TPUs and large-scale infrastructure</td>
  </tr>
  <tr>
    <td><strong>Training Cost</strong></td>
    <td>Lower cost due to smaller datasets and fewer resources</td>
    <td>Extremely expensive due to vast datasets and high training complexity</td>
  </tr>
  <tr>
    <td><strong>Performance in General Tasks</strong></td>
    <td>Specialized performance, optimized for specific domains</td>
    <td>Strong general-purpose capabilities, excelling in diverse NLP tasks</td>
  </tr>
  <tr>
    <td><strong>Accuracy & Precision</strong></td>
    <td>High accuracy within a specific domain (e.g., finance)</td>
    <td>High accuracy in general NLP but prone to hallucinations in specialized fields</td>
  </tr>
  <tr>
    <td><strong>Data Efficiency</strong></td>
    <td>Requires fewer data for training and fine-tuning</td>
    <td>Needs massive datasets for training and generalization</td>
  </tr>
</table>
<h3>Approaches and Techniques in Previous Research</h3>

<p>The first part of the review covers preliminary knowledge in several approaches and techniques in previous research:</p>

<ul>
    <li>
        <strong>Optimization Techniques:</strong> Methods such as quantization, pruning, imitation learning, progressive learning, knowledge distillation, and reasoning distillation are explored as strategies to enhance the efficiency of SLMs. These techniques allow smaller models to achieve comparable performance to LLMs while significantly reducing computational demands.
    </li>
    <li>
        <strong>Hallucination Mitigation:</strong> One of the primary concerns in financial AI applications is the generation of hallucinated or incorrect data. The paper discusses mitigation strategies, including Retrieval-Augmented Generation (RAG) and explanation tuning, which help improve the factual accuracy of model outputs. Additionally, hybrid approaches combining fine-tuned question models and RAG are examined.
    </li>
    <li>
        <strong>Evaluation Metrics:</strong> The review details various evaluation metrics applicable to SLMs, including perplexity, BLEU, TER, ROUGE, hallucination score, and domain-specific financial metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). These metrics are essential for assessing model performance in text generation, prediction, and information retrieval tasks. Additionally, financial benchmarks for accurate evaluation are discussed.
    </li>
    <li>
        <strong>Challenges in Financial SLMs:</strong> The review highlights critical challenges, such as data security, hallucination, and ethical concerns in deploying SLMs in financial applications. Financial data security is particularly emphasized, with discussions on private hosting solutions, federated learning, and differential privacy as potential safeguards.
    </li>
    <li>
        <strong>Domain-Specific Applications:</strong> The paper explores how SLMs are tailored for industry-specific applications, including medical, legal, retail, and financial domains. In finance, SLMs support market prediction, financial report analysis, and automated customer interactions. The importance of domain-specific fine-tuning to enhance model accuracy is underscored.
    </li>
</ul>
<h3>Advancements in Financial Language Models: Performance, Applications, and Trade-offs</h3>
Recent advancements in language models (LMs) have significantly improved financial tasks such as sentiment analysis, financial forecasting, and risk management. Specialized models like FINBERT (2022), BloombergGPT, and FinGPT cater specifically to financial NLP challenges, handling complex terminology and numerical data.
<h3>Key Models & Capabilities:</h3>
<ul>
    <li><strong>BloombergGPT (50B parameters):</strong>A large-scale proprietary model for financial analysis.</li>
    <li><strong>FinGPT (7B & 13B):</strong>Open-source, excelling in financial document summarization and question answering.</li>
    <li><strong>FINBERT (110M):</strong>Optimized for sentiment analysis and financial entity recognition.</li>
    <li><strong>InvestLM (65B):</strong>Trained on CFA exam questions and SEC filings for financial classification.</li>
</ul>

While larger models like BloombergGPT offer superior accuracy, smaller models (e.g., Google-Gemma-2B, OpenELM-270M) are more resource-efficient but struggle with complex tasks. 

<h3>Model parameters count and capabilities of language models</h3>

<table>
    <thead>
        <tr>
            <th>Finance-Specific Language Models</th>
            <th>Model Parameters</th>
            <th>Model Capabilities</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>BloombergGPT 50B<br>Dataset: FinPile</td>
            <td>50B</td>
            <td>
                <ul>
                    <li>Sentiment analysis</li>
                    <li>Named entity recognition</li>
                    <li>Question answering</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>FinBERT (open)<br>Dataset: Financial PhraseBank</td>
            <td>110M</td>
            <td>
                <ul>
                    <li>Sentiment analysis</li>
                    <li>Financial entity recognition</li>
                  <li>Financial classification tasks</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>FLANG (open)</td>
            <td>110M</td>
            <td>
                <ul>
                    <li>Sentiment analysis</li>
                    <li>Named entity recognition</li>
                    <li>Document classification</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>InvestLM (fine-tuned LLaMA-open)<br>Dataset: CFA, SEC</td>
            <td>65B</td>
            <td>
                <ul>
                    <li>Sentiment analysis</li>
                    <li>Financial text classification</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>FinMA (fine-tuned LLaMA-open)<br>Dataset: PIxIU</td>
            <td>7B and 13B</td>
            <td>
                <ul>
                    <li>Sentiment analysis</li>
                    <li>Financial document summarization</li>
                    <li>Question answering</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>FinGPT (open)<br>Dataset: FinQA, FinRed</td>
            <td>7B and 13B</td>
            <td>
                <ul>
                    <li>Financial document summarization</li>
                    <li>Question answering</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Google-gemma 2B</td>
            <td>2B</td>
            <td>
                <ul>
                    <li>Financial text classification</li>
                    <li>Financial document summarization</li>
                    <li>Question answering</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>TinyLlama (fine-tuned LLaMA)</td>
            <td>1.1B</td>
            <td>
                <ul>
                    <li>Financial text classification</li>
                    <li>Financial document summarization</li>
                    <li>Question answering</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Apple-OpenELM<br>Dataset: RefinedWeb, Pile</td>
            <td>270M - 3B</td>
            <td>
                <ul>
                    <li>Sentiment analysis</li>
                    <li>Named entity recognition (NER)</li>
                    <li>Document classification</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Microsoft-phi</td>
            <td>1B - 3B</td>
            <td>
                <ul>
                    <li>Sentiment analysis</li>
                    <li>Named entity recognition (NER)</li>
                    <li>Document classification</li>
                    <li>Question answering</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

## Methodology

<img src="https://raw.githubusercontent.com/cepdnaclk/e19-4yp-Developing-a-Small-Scale-Financial-Language-Model/main/docs/images/im.png" alt="Desc" width="600">

## Experiment Setup and Implementation

## Results and Analysis

## Conclusion

## Publications
[//]: # "Note: Uncomment each once you uploaded the files to the repository"

<!-- 1. [Semester 7 report](./) -->
<!-- 2. [Semester 7 slides](./) -->
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/e19-4yp-Developing-a-Small-Scale-Financial-Language-Model)
- [Project Page](https://cepdnaclk.github.io/e19-4yp-Developing-a-Small-Scale-Financial-Language-Model/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
