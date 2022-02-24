#!/usr/bin/python3

# Mathematics and Big Data - Text Mining Practice 2
# Universitat Autonoma de barcelona
# All rights reserved.

# Importing the Python libraries
# To install a Python Package
# pip install package_to_install

import sklearn
import os
import scipy
import numpy as np
import matplotlib.pyplot as plt # https://stackoverflow.com/questions/45150238/error-with-matplotlib-show-module-matplotlib-has-no-attribute-show/45150262
from wordcloud import WordCloud # https://stackoverflow.com/questions/47980656/wordcloud-is-not-defined-python3-6
import textmining # https://pypi.org/project/textmining3/
import string
import sklearn
import math
import string
import sys
import re
import pandas as pd
import sklearn.feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

path = "/Users/mac06/Code/MBD/Excercise2/tweets.txt"

# read corpus by path
def read_corpus(path):
    try:
        with open(path, 'r') as f:
            data = []
            lines = f.readlines()
            for line in lines:
                line = line.encode().decode()
                data.append(line)
        return data

    except IOError:
        print("Error opening or reading input file: ", path)
        sys.exit()

# Text Cleaning and Preprocessing
def preprocess(doc):
    # Remove mentions
    doc = re.sub("@\S+", "", doc)

    # Remove tickers
    doc = re.sub("NT\$", "", doc)
    doc = re.sub("\$", "", doc)

    # Remove urls
    doc = re.sub("https?:\/\/.*[\r\n]*", "", doc)

    # Remove hashtags
    doc = re.sub("#", "", doc)

    # Remove Punctuations
    doc = doc.translate(str.maketrans('', '', string.punctuation))

    # White Space removal
    doc = doc.strip()

    # Remove starting with "b"
    if doc == 'b':
        doc = ""
    elif doc[0] == 'b' and doc[1].isupper():
        doc = doc[1:]

    # Remove double space
    doc = re.sub(' +', ' ', doc)
    doc = re.sub(' ,', ',', doc)

    # return new doc
    return doc

def relevant(corpus):
    time = 0
    relevant_word = []
    dic={}
    for document in corpus:
        for word in document.split():
            dic[word] = dic.get(word, 0) + 1
            if dic[word] > time:
                time = dic[word]
                relevant_word = [word]
            elif dic[word] == time:
                time = dic[word]
                relevant_word.append(word)
    return relevant_word

# Choose font and background options in function visualize as follows:
def visualize(text, save = False):
    wordcloud = WordCloud(max_font_size=50, max_words=100).generate(text)

    # Save the image in the img folder:
    if save:
        wordcloud.to_file("first_document.png")

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    # Generting documents
    corpus = read_corpus(path)

    for idx, doc in enumerate(corpus):
        d = preprocess(doc)
        # print("="*10)
        # print(doc)
        # print(d)
        corpus[idx] = d

    # Document Term Matrix
    tdm = textmining.TermDocumentMatrix()

    # Creating TDM for each document
    for doc in corpus:
        tdm.add_doc(doc)

    # for row in tdm.rows(cutoff=1):
    #     print(row)

    # Writing TDM in csv file
    tdm.write_csv('matrix.csv', cutoff = 1)

    # Finding TDM by using sklearn Package
    vec = CountVectorizer()
    X = vec.fit_transform(corpus)
    df = pd.DataFrame(X.toarray(), columns = vec.get_feature_names())
    # print(df)

    # Find the most relevant words
    print("Find the most relevant words:", relevant(corpus))

    ############# Text Visualization ##############
    # Join all of the documents
    document = ''.join([i for i in corpus])

    ##### WordCloud  #######
    # To visualize the word cloud for text
    visualize(document)