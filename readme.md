# 🤖 Real-Time Sentiment-Aware Chatbot with Voice and Emoji UI

This is a Flask-based AI chatbot that performs real-time sentiment analysis using `TextBlob`, responds accordingly with context-aware messages, and includes an enhanced frontend featuring:

- 😃 Emoji-based responses
- 💬 Typing animation
- 🎤 Voice input (via Html)
- 🔊 Voice output using Html

---

## 🧠 Features

- Sentiment analysis using **TextBlob**
- Preprocessed small dataset (CSV with 50 samples)
- Custom contextual replies based on sentiment (`positive`, `neutral`, `negative`)
- Frontend chat UI with:
  - Typing animation ⌨️
  - Emojis in messages 😞😂😍
  - Voice input 🎙️ (browser)
  - Voice output 🔊 (via Html)
---

## 📁 Project Structure
internshiptask19/
┣ 📄 app.py # Flask backend
┣ 📄 sentiment_data.csv # Small sentiment dataset
┣ 📄 requirements.txt # All dependencies
┣ 📄 README.md # This file
┣ 📂 templates/
┃ ┗ 📄 index.html # Chat UI frontend

## Install Dependencies
pip install -r requirements.txt

## You must also have nltk and textblob resources:

import nltk
nltk.download('punkt')
nltk.download('stopwords')

## Run the Flask App
python app.py
Visit: http://127.0.0.1:5000

