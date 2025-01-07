# Hotel Review Sentiment Analysis

This is a sentiment analysis project developed using Flask. The model performs sentiment analysis on hotel reviews, categorizing them as positive, neutral, or negative based on the text input. The user interface is built using Flask, where users can input hotel reviews and receive sentiment predictions in real-time.

## Features

- **Sentiment Classification**: Classifies hotel reviews as positive, negative, or neutral.
- **User Interface**: A simple Flask-based web interface where users can submit hotel reviews and view the sentiment analysis results.
- **Real-time Predictions**: The model predicts the sentiment of the review as soon as it is submitted.

## Installation

To run this project locally, follow the steps below:

### Prerequisites

- Python 3.x
- Flask
- Scikit-learn (or another machine learning library for your sentiment analysis model)
- Pandas
- Numpy

### Steps to Run the Project Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hotel-review-sentiment-analysis.git

2.Navigate to the project directory:
   ```bash
   cd hotel-review-sentiment-analysis

3.Install the required packages:
   ```bash
   pip install -r requirements.txt

4.Run the Flask app:
   ```bash
   python app.py

##How It Works
-The Flask application provides a simple form where users can input hotel reviews.
-Once a review is submitted, the input text is passed through a pre-trained sentiment analysis model to determine the sentiment.
-The model returns the sentiment as positive, negative, or neutral, and the result is displayed on the webpage.
##Model Details
The sentiment analysis model is a machine learning model trained on a dataset of hotel reviews. The model uses text preprocessing techniques like tokenization, stopword removal, and feature extraction (e.g., TF-IDF) to classify the sentiment of the review.

