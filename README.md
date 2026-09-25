# 📧 Email Spam Detection using SVM

A Machine Learning-based Email Spam Detection system that classifies text messages as **Spam** or **Ham (Not Spam)** using **TF-IDF Vectorization** and a **Support Vector Machine (SVM)** classifier.

The trained ML model is integrated with a **FastAPI backend** and a simple web interface for real-time prediction.

---

## 🚀 Project Overview

Spam messages are unwanted messages that may contain advertisements, scams, fraudulent offers, or malicious links.

This project uses Natural Language Processing (NLP) and Machine Learning to automatically classify a message as:

- 🚨 **Spam**
- ✅ **Ham (Not Spam)**

The system takes a text message as input, converts it into numerical features using **TF-IDF**, and then uses a trained **SVM classifier** to make the prediction.

---

## 🧠 How It Works

The system follows this pipeline:

```text
User Message
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
SVM Classifier
     ↓
Spam / Ham Prediction
     ↓
FastAPI Response
     ↓
Web Interface

## 🖥️ Application Screenshots

### 🚨 Spam Detection

The application successfully identifies suspicious messages as spam.

![Spam Detection](static/screenshots/spam-result.png)

### ✅ Ham Detection

Normal messages are classified as ham (not spam).

![Ham Detection](static/screenshots/ham-result.png)