from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from pymongo import MongoClient
import os

df = pd.read_csv("sentiment_data.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

model = LogisticRegression(max_iter=1000)
model.fit(X, y)


client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot"]
chatlog = db["chatlog"]

app = Flask(__name__)

def analyze_sentiment(text):
    X_input = vectorizer.transform([text])
    prediction = model.predict(X_input)[0]

    if prediction == "positive":
        reply = "That's great to hear! 😊"
    elif prediction == "negative":
        reply = "I'm sorry to hear that. Want to talk more about it?"
    else:
        reply = "Thanks for sharing. Is there anything else I can help with?"

    return prediction, reply

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()  # Parse JSON from request body
    user_msg = data.get('msg', '') 
    sentiment, bot_reply = analyze_sentiment(user_msg)

    # Save to MongoDB
    chatlog.insert_one({
        "user_input": user_msg,
        "sentiment": sentiment,
        "bot_reply": bot_reply
    })

    return jsonify({'reply': bot_reply, 'sentiment': sentiment})

if __name__ == "__main__":
    app.run(debug=True)
