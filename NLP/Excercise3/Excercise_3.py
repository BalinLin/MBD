#!/usr/bin/python3

# Mathematics and Big Data - Text Mining Practice 3
# Universitat Autonoma de barcelona
# All rights reserved.

# Importing the Python libraries
import spacy
from spacy import displacy
import nltk
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

path = "/Users/mac06/Code/MBD/Excercise2/tweets.txt"

# read corpus by path
def read_corpus(path):
    try:
        with open(path, 'r') as f:
            data = f.read()
        return data

    except IOError:
        print("Error opening or reading input file: ", path)
        sys.exit()

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    # doc_file = read_corpus(path)
    doc_file = "I'am Balin Lin from Taiwan. My email is email@ntust.tw. Studying at uab. Url: https://www.uab.cat/web/universitat-autonoma-de-barcelona-1345467954774.html"

    doc = nlp(doc_file)
    print("My document:\n{0}".format(doc))

    print("\nMy tokens: (text, pos_, dep_)")
    for token in doc:
        print(token.text, token.pos_, token.dep_)

    print("\nMy ents:\n{0}".format(doc.ents))
    for ent in doc.ents:
        print(ent.text, ent.label_, str(spacy.explain(ent.label_)))

    print("\nMy noun chunks:\n{0}".format(doc.noun_chunks))
    for chunk in doc.noun_chunks:
        print(chunk)

    # Display on jupyter
    # spacy.displacy.render(doc, style='dep', jupyter=True, options={'distance': 100})

    words = ['run', 'ran', 'running', 'buy', 'bought', 'cared','university','fairly','easily','singing', 'sings','sung','singer','sportingly']

    print("\nStemming/Lemmatization:")
    ps = PorterStemmer()
    print(' '.join(ps.stem(s) for s in words))

    print("\nStemming/Lemmatization 2:")
    ss = SnowballStemmer(language='english')
    print(' '.join(ss.stem(s) for s in words))

    print("\nStop words:")
    print(nlp.Defaults.stop_words) # Member function: (is_stop, add, remove)
