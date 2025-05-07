import pandas as pd
import numpy as np
import re
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# ========== 1. Load Dataset ==========
df = pd.read_csv("bbc-text.csv")  # columns: 'category', 'text'

# ========== 2. Preprocessing ==========
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"\@w+|\#", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = " ".join([stemmer.stem(word) for word in text.split() if word not in stop_words])
    return text

df["clean_text"] = df["text"].apply(clean_text)

# ========== 3. Split ==========
X_train, X_test, y_train, y_test = train_test_split(df["clean_text"], df["category"], test_size=0.2, random_state=42)

# ========== 4. TF-IDF + Classifier Pipeline ==========
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("clf", MultinomialNB())
])

pipeline.fit(X_train, y_train)

# ========== 5. Evaluation ==========
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
