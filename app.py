from flask import Flask, render_template, request
import pandas as pd
import joblib
import nltk
import re

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model and vectorizer
model = joblib.load('rmodel.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Preprocessing function
def preprocess(r1):
    r1 = r1.lower()
    r1 = re.sub('[^a-z]', ' ', r1)
    words = [word for word in r1.split() if word not in nltk.corpus.stopwords.words('english')]
    return ' '.join(words)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default response for the form
    prediction = None
    if request.method == 'POST':
        # Get the review text from the form
        review = request.form['review']
        
        # Preprocess the review and transform it into the vector space model
        processed_review = preprocess(review)
        X_test = vectorizer.transform([processed_review]).toarray()
        
        # Predict the sentiment (positive/negative)
        prediction = model.predict(X_test)[0]
        
        # Convert prediction to a string for user-friendly display
        sentiment = "Positive" if prediction == 1 else "Negative"

        return render_template('index.html', sentiment=sentiment)
    
    return render_template('index.html', sentiment=prediction)

if __name__ == "__main__":
    app.run(debug=True)
