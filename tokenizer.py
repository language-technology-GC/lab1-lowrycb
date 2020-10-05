#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:49:55 2020

@author: cass_lowry
"""

import nltk

assert nltk.download("punkt")

# tokens = nltk.word_tokenize("This is a test.")

tokens = []
with open("/Users/cass_lowry/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/data/news.2015.en.shuffled.deduped", "r") as source:
    for line in source:
        tokens += nltk.word_tokenize(line) # should have used .append()
        


with open("/Users/cass_lowry/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/data/news.2015.en.shuffled.deduped.tokenized.txt", "w") as sink:
    # The keyword argument `file` sends the data to a file handle
    # opened for writing.
    for token in tokens:
        print(token, file=sink)

#%% removing judgement column from target words and writing new tsv
        
import pandas as pd

df = pd.read_csv("~/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/data/ws353.tsv", sep='\t',
                 header=None)

df.to_csv('~/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/wordpairs.tsv', 
          sep = '\t',
          columns = (0,1),
          header = False,
          index = False)

#%%

tokenized_sentences = []
with open("/Users/cass_lowry/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/test_sentences.txt", "r") as source:
    for line in source:
        tokenized_sentences.append(nltk.word_tokenize(line))
        
# print(tokenized_sentences)

with open("/Users/cass_lowry/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/test_tokenized.txt", "w") as sink:
    for sentence in tokenized_sentences:        
        printable_tokens = ""
        for token in sentence:
            printable_tokens += (token+" ")
        print(printable_tokens, file=sink)

#%% new way
        
tokenized_sentences = []
with open("/Users/cass_lowry/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/data/news.2015.en.shuffled.deduped", "r") as source:
    for line in source:
        tokenized_sentences.append(nltk.word_tokenize(line))

with open("/Users/cass_lowry/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/data/news.2015.en.shuffled.deduped.tokenized.txt", "w") as sink:
    for sentence in tokenized_sentences:        
        printable_tokens = ""
        for token in sentence:
            printable_tokens += (token+" ")
        print(printable_tokens, file=sink)