# NLP course's assignments
This repository contains 3 assignments of the NLP subject.

## Assignment 1
### `as1.ipynb`

This notebook focuses on **text preprocessing and basic statistical NLP tasks**, such as word frequency analysis, tokenisation, and Zipf's law visualization. 
It demonstrates how to clean and normalise raw text data, generate frequency distributions, and explore vocabulary size in corpora using Python and NLTK.

---

## Assignment 2
### `as2.ipynb`
This notebook implements a **trigram language model** using **Maximum Likelihood Estimation (MLE)** and evaluates it on sentence prediction tasks. 
It includes procedures for calculating smoothed probabilities (add-k smoothing), perplexity evaluation, and comparisons with other N-gram models, offering insight into core concepts in probabilistic language modeling.

---
## Assignment 3

This project implements an **automated fact-checking system** designed to evaluate climate-related claims using evidence retrieved from a large textual corpus. The task is structured as a **retrieval + classification** pipeline, where the model must first identify relevant evidence passages and then classify the claim as one of: `SUPPORTS`, `REFUTES`, `NOT_ENOUGH_INFO`, or `DISPUTED`.
It emphasizes **novel model design and justification** over raw performance, with marks awarded for thoughtful architecture choices and evaluation. The retrieval and classification components must be built using allowed neural architectures (RNN, LSTM, GRU, or Transformer), and all training must adhere to strict reproducibility and hardware constraints.


### 📁 Files:
- Code: `40-comp90042-project-2025.ipynb`
- Dataset:
  * `train-claims.json`, `dev-claims.json`: Labeled data for training and validation.
  * `test-claims-unlabelled.json`: Test claims for leaderboard submission.
  * `evidence.json`: Corpus of evidence passages.
  * `eval.py`: Official evaluation script for scoring predictions.
- Report: COMP90042_40.pdf

### 🔍 Task Objectives:
1. **Evidence Retrieval** – Find relevant passages for a given claim from the corpus.
2. **Claim Classification** – Determine the factual status of the claim based on retrieved evidence.


### 📊 Evaluation Metrics:
* **Evidence Retrieval F-score**
* **Claim Classification Accuracy**
* **Harmonic Mean** (used for leaderboard ranking)
