import pandas as pd

# regex
import re

# NLTK
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# TextBlob
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')


def tokenize(string):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(string)
    return tokens


def intoEnglish(string):
    blob = TextBlob(string)
    lang = blob.detect_language()

    if lang == 'es':
        try:
            english_blob = blob.translate(from_lang='es', to='en')
            return "".join(list(english_blob))
        except:
            return string
    else:
        return string


def stop_words(lista):
    stop_words = set(stopwords.words('english'))
    nueva_lista = []
    for string in lista:
        if string not in stop_words:
            nueva_lista.append(string)
    return " ".join(nueva_lista)


def sentiment(phrase):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(phrase)
    pol = polarity['compound']
    return pol


def process_language(message):
    english_msg = intoEnglish(message)
    print(english_msg)
    english_msg_list = english_msg.split(' ')
    clean_eng_msg = stop_words(english_msg_list)
    print(clean_eng_msg)
    result = sentiment(clean_eng_msg)
    return result
