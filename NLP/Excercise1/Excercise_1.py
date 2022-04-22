#!/usr/bin/python3
# coding=utf-8

# Mathematics and Big Data - Text Mining Excercise 1
# Universitat Autonoma de barcelona

# Importing the Python libraries
import pandas as pd
import sklearn
import re
import string

# Create Corpus
corpus = [
    "Pineapple cake (Chinese: 鳳梨酥; pinyin: fènɡ lí sū; Taiwanese Hokkien: 王梨酥 ông-lâi-so͘) is a sweet traditional Taiwanese pastry containing butter, flour, egg, sugar, and pineapple jam or slices.",
    "Pineapple became a critical component of Taiwan's economy during the Japanese era, during which Japanese industrialists imported a wide variety of pineapple cultivars and established numerous processing plants.[2]",
    "By the late 1930s, Taiwan had become the third-largest exporter of pineapples in the world.[2]",
    "However, when pineapple production in Taiwan shifted toward domestic sales and use of fresh pineapple, local bakeries sought to use this surplus in pastries.[3]",
    "While pineapple cakes had historically been produced as a ceremonial food, a combination of governmental promotion and globalization popularized the pineapple cake.",
    "Pineapple cakes have become one of the top-selling souvenirs in Taiwan.[4]",
    "Since 2005, the Taipei City Government has run an annual Taipei Pineapple Cake Cultural Festival to foster the growth the local tourism industry and promote sales of the pineapple cake.[5][6]",
    "In 2013, the revenue from Taiwan's pineapple cake bakeries totaled NT$40 billion (US$1.2 billion), and sales of pineapple cakes have also bolstered agricultural economies in rural parts of the country.[7][3]"
]
corpus_new = []

# Text Cleaning and Preprocessing
l = ['{', '[', '(']
r = ['}', ']', ')']

print("Before Cleaning:")
for d in corpus:
    print(d)

for idx, doc in enumerate(corpus):
    # White Space removal
    doc = doc.strip()

    # Remove text in braces, brackets, parentheses.
    for i in range(len(l)):
        left = doc.find(l[i])
        while left != -1:
            right = doc.find(r[i])
            doc = doc[:left] + doc[right+1:]
            left = doc.find(l[i])

    # Remove mentions
    doc = re.sub("@\S+", "", doc)

    # Remove tickers
    doc = re.sub("NT\$", "", doc)
    doc = re.sub("\$", "", doc)

    # Remove urls
    doc = re.sub("https?:\/\/.*[\r\n]*", "", doc)

    # Remove hashtags
    doc = re.sub("#", "", doc)

    # Remove double space
    doc = re.sub(' +', ' ', doc)
    doc = re.sub(' ,', ',', doc)

    # Create new corpus
    corpus_new.append(doc)

print("-" * 30)
print("After Cleaning:")
for d in corpus_new:
    print(d)

### Output:
# Before Cleaning:
# Pineapple cake (Chinese: 鳳梨酥; pinyin: fènɡ lí sū; Taiwanese Hokkien: 王梨酥 ông-lâi-so͘) is a sweet traditional Taiwanese pastry containing butter, flour, egg, sugar, and pineapple jam or slices.
# Pineapple became a critical component of Taiwan's economy during the Japanese era, during which Japanese industrialists imported a wide variety of pineapple cultivars and established numerous processing plants.[2]
# By the late 1930s, Taiwan had become the third-largest exporter of pineapples in the world.[2]
# However, when pineapple production in Taiwan shifted toward domestic sales and use of fresh pineapple, local bakeries sought to use this surplus in pastries.[3]
# While pineapple cakes had historically been produced as a ceremonial food, a combination of governmental promotion and globalization popularized the pineapple cake.
# Pineapple cakes have become one of the top-selling souvenirs in Taiwan.[4]
# Since 2005, the Taipei City Government has run an annual Taipei Pineapple Cake Cultural Festival to foster the growth the local tourism industry and promote sales of the pineapple cake.[5][6]
# In 2013, the revenue from Taiwan's pineapple cake bakeries totaled NT$40 billion (US$1.2 billion), and sales of pineapple cakes have also bolstered agricultural economies in rural parts of the country.[7][3]
# ------------------------------
# After Cleaning:
# Pineapple cake is a sweet traditional Taiwanese pastry containing butter, flour, egg, sugar, and pineapple jam or slices.
# Pineapple became a critical component of Taiwan's economy during the Japanese era, during which Japanese industrialists imported a wide variety of pineapple cultivars and established numerous processing plants.
# By the late 1930s, Taiwan had become the third-largest exporter of pineapples in the world.
# However, when pineapple production in Taiwan shifted toward domestic sales and use of fresh pineapple, local bakeries sought to use this surplus in pastries.
# While pineapple cakes had historically been produced as a ceremonial food, a combination of governmental promotion and globalization popularized the pineapple cake.
# Pineapple cakes have become one of the top-selling souvenirs in Taiwan.
# Since 2005, the Taipei City Government has run an annual Taipei Pineapple Cake Cultural Festival to foster the growth the local tourism industry and promote sales of the pineapple cake.
# In 2013, the revenue from Taiwan's pineapple cake bakeries totaled 40 billion, and sales of pineapple cakes have also bolstered agricultural economies in rural parts of the country.