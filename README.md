## Intent-Detection-System-Fine-Tuning-DistilBERT-for-High-Performance-


This application is designed to detect the user’s intent from a short text message using a fine-tuned transformer model (DistilBERT). It leverages Natural Language Processing (NLP) techniques to understand what the user wants to do—whether it’s booking a restaurant, getting weather info, or playing music.

---

## 📖 Overview

This project allows users to type a message and receive an instant prediction of their intent. It is built for educational and experimental purposes in NLP and intent detection.

---

## 📂 Features

- ✂️ **Text Preprocessing**: Lowercases text and removes English stopwords  
- 🤗 **Transformers Integration**: Uses HuggingFace’s DistilBERT model  
- 🎯 **Intent Prediction**: Classifies text into one of several predefined intent categories  
- 🖥️ **Streamlit UI**: Clean and responsive real-time web interface  
- 📥 **Interactive Input Field**: Users can type any message and receive intent prediction instantly  

---

## 🛠️ Methodology

### 🧹 Text Preprocessing

- Converts all text to lowercase  
- Removes English stopwords using NLTK  

### 🔍 Prediction Logic

- Tokenizes input text with `DistilBertTokenizer`  
- Uses a fine-tuned `DistilBertForSequenceClassification` model to generate logits  
- Applies `argmax` to identify the predicted intent class  

### 💻 Web Interface

- Built using Streamlit  
- Displays a single input field for the user  
- Shows the predicted intent after pressing the "Predict Intent" button  

---

## 🧠 Intent Categories

- `get weather`  
- `search creative work`  
- `search screening event`  
- `add to playlist`  
- `book restaurant`  
- `rate book`  
- `play music`  

---

## 📊 Example Output

**User Input:**  
```
I want to reserve a table for two
```

**Predicted Intent:**  
```
book restaurant
```

---

## 🚀 Installation & Usage

### 📦 Requirements

- Python 3.x  
- Streamlit  
- Transformers  
- PyTorch  
- NLTK  

### 🔧 Setup

```bash
pip install streamlit transformers torch nltk
```

### ▶️ Running the App

1. Ensure your trained model is saved and accessible at the `"token + model"` path  
2. Save your Python script as `app.py`  
3. Launch the app with:

```bash
streamlit run app.py
```

4. Open the app in your browser and start typing!

---

## 📌 Future Improvements

- 🧠 Expand the intent classification categories  
- 📱 Create a mobile-friendly interface  
- 🧾 Add context tracking and session memory  
- 🌍 Support for multilingual input  

---

🚀 **Explore how NLP can help machines understand your intent in real-time!**
