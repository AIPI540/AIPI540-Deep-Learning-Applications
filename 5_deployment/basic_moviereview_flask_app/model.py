import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import pickle
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def process_text(review):
    # Extract text from html
    review_text = BeautifulSoup(review,features="html.parser").get_text()
    # Remove non-letters
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    # Convert words to lower case and split them
    words = review_text.lower().split()
    # Remove stopwords
    stops = set(stopwords.words("english"))
    words = [w for w in words if not w in stops]
    review_processed = " ".join(words)
    return review_processed


def train(X_train, y_train):
    # Pre-process text
    X = X_train.apply(lambda x: process_text(x))
    # Transform text to features
    vect = TfidfVectorizer()
    vect.fit(X)
    X_featurized = vect.transform(X)
    # Train model
    model = RandomForestClassifier()
    model.fit(X_featurized, y_train)
    # Save model and vectorizer
    pickle.dump(model, open('./models/model.pkl','wb'))
    pickle.dump(vect, open('./models/vect.pkl','wb'))
    return

def predict(review, model, vect):
    label = {0: 'negative', 1: 'positive'}
    review = process_text(review)
    X = vect.transform([review])
    y = model.predict(X)[0]
    proba = np.max(model.predict_proba(X))
    return label[y], proba

if __name__ == '__main__':
    # Run model training
    train_data = pd.read_csv('data/labeledTrainData.tsv',header=0,delimiter='\t',quoting=3)
    X_train = train_data['review']
    y_train = train_data['sentiment']
    train(X_train,y_train)
    print('Training complete')

