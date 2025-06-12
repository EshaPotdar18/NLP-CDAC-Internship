# NLP Internship at CDAC (May–June 2025)

This repository provides a high-level overview of the work I completed during my internship at the Centre for Development of Advanced Computing (CDAC), Pune, focused on agentic AI pipelines, speech-to-text systems, and custom summarization and refinement modules.

---

## 🚀 Project Scope

The goal of the internship was to develop and test components of a system that:
- Transcribes speech audio using a transformer-based STT model
- Summarizes the transcriptions using a fine-tuned LLM
- Performs custom translation and refinement
- Integrates Retrieval-Augmented Generation (RAG) pipelines for legal document processing

---

## 🧠 Key Technologies

- `Python`, `PyTorch`
- `Transformers`, `Hugging Face`
- `SpeechRecognition`, `Wav2Vec2`, `Whisper`
- `Summarization Models`: BART, T5
- `RAG`: Embedding + Vector DB + QA
- `UMAP`, `Visdom`, `Matplotlib` for visualizations
- `FastAPI` for API deployment

---

## 🏗️ Project Architecture

```text
Audio Input ➜ Speech-to-Text ➜ Summarization ➜ Translation ➜ Refinement ➜ RAG ➜ Output
