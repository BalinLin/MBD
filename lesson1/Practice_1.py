#!/usr/bin/python3
# coding=utf-8

# Python Installation Resources:

# https://docs.anaconda.com/anaconda/install/windows/
# https://www.jcchouinard.com/install-python-with-anaconda-on-windows/
# https://phoenixnap.com/kb/how-to-install-python-3-windows
# https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html


# Mathematics and Big Data - Text Mining Practice 1
# Universitat Autonoma de barcelona
# All rights reserved.

# Importing the Python libraries


import pandas as pd
import sklearn
import re
import string

# Text Cleaning and Preprocessing

# Case Normalization

# convert text to lowercase

doc1 = "The 5 biggest countries by population in 2020 are China, India, United States, Indonesia, and Brazil."
doc_str = doc1.lower()
print(doc_str)

# Remove numbers

doc2 = "Boul A contains 4 red and 6 white balls, while Boul B contains 3 red and 4 blue balls."
result = re.sub(r'\d+', '', doc2)
print(result)


# Remove Punctuations
# The following code removes this set of symbols

doc3 = "This &is [an] example? {of} string. with.? punctuation!!!!" # Sample string
# result = doc3.translate(string.maketrans("",""), string.punctuation)
result = doc3.translate(str.maketrans("",""))
print(result)

# White Space removal

doc = " \t a string example\t "
doc_str = doc.strip()
doc_str



# StopWords Removal

text = "The lockdown restrictions will be dropped in the summer so we can go partying again!"
stop_words = []
# removing stopwords
text = " ".join([word for word in text.split() if word not in stop_words])
print(text)


# Removing URLs, Hashtags, Punctuation, Mentions, etc

# removing mentions

text = "You should get @BlockFiZac from @BlockFi to talk about bitcoin lending, stablecoins, institution adoption, and the future of crypto"

text = re.sub("@\S+", "", text)
print(text)

#Output: You should get  from  to talk about bitcoin lending, stablecoins, institution adoption, and the future of crypto


# remove tickers

text = """#BITCOIN LOVES MARCH 13th A year ago the price of Bitcoin collapsed to $3,800 one of the lowest levels in the last 4 years. Today, exactly one year later it reaches the new all-time high of $60,000 Thank you Bitcoin for always making my birthday exciting"""

text = re.sub("\$", "", text)
print(text)

#Output: #BITCOIN LOVES MARCH 13th A year ago the price of Bitcoin collapsed to  3,800 one of the lowest levels in the last 4 years. Today, exactly one year  later it reaches the new all-time high of 60,000 Thank you Bitcoin for  always making my birthday exciting

# remove urls


text = "Did someone just say “Feature Engineering”? https://buff.ly/3rRzL0s"

text = re.sub("https?:\/\/.*[\r\n]*", "", text)
print(text)

# Output: Did someone just say “Feature Engineering”?

# removing hashtags

text = """.#FreedomofExpression which includes #FreedomToProtest should be the cornerstone of any democracy. I’m looking forward to speaking in the 2 day debate on the #PoliceCrackdownBill & explaining why I will be voting against it."""


text = re.sub("#", "", text)
print(text)


#Output: FreedomofExpression which includes FreedomToProtest should be the  cornerstone of any democracy. I’m looking forward to speaking in the 2 day  debate on the PoliceCrackdownBill & explaining why I will be voting against it.

