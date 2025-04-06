import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# load save model
model = DistilBertForSequenceClassification.from_pretrained("token + model")
tokenizer = DistilBertTokenizer.from_pretrained("token + model")

stop_words = set(stopwords.words('english'))

def preprocess_text(text):

  # convert to lowercase
  text = text.lower()

  # remove stopwords
  text = ' '.join([word for word in text.split() if word not in stop_words])

  return text


def predict(text, model, tokenizer, max_length=22):

  #lower case and remove stopwords
  text = preprocess_text(text)

  #tokenize
  inputs = tokenizer(text, padding='max_length', truncation=True, max_length=max_length, return_tensors='pt')

  with torch.no_grad():
    outputs = model(**inputs)
    outputs = outputs.logits

  predicted_label = torch.argmax(outputs, dim=1).item()

  return predicted_label

# UI App...
st.title("Intent-Detection System")

text = st.text_input("type your message here...")

if st.button("Predict Intent"):
    if text:
        id = predict(text, model, tokenizer)

        label = {
            5: 'get weather',
            0: 'search creative work',
            1: 'search screening event',
            3: 'add to playlist',
            6: 'book restaurant',
            4: 'rate book',
            2: 'play music'

        }

        intent = label.get(id, "unknown intent")

        st.write("Predicted intent :", intent)
    else:
        st.write("type your message again")



