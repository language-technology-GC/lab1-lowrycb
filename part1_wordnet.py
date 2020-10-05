#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:00:59 2020

@author: cass_lowry
"""

#%%
# wordnet code examples from https://github.com/alvations/wordnet
import numpy as np
import pandas as pd

from wn import WordNetError # had to import this to define WordNetError

from scipy import stats

from wn import WordNet
from wn.info import WordNetInformationContent

from wn.constants import wordnet_30_dir#, wordnet_33_dir
wordnet = WordNet(wordnet_30_dir) # Uses WordNet v3.0 to be comparable to NLTK, by default uses v3.3
#%% reading in human judgmements 

df = pd.read_csv("~/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/data/ws353.tsv", sep='\t',
                 header=None,
                 names=['w1', 'w2', 'judgement'])
print(df)


#%% learning how to index pandas

df2 = df
df2['path'] = None # PROBLEM, I don't understand why changes to df2 are reflected in df as well

df2.loc[df2.index[[0,1,2,3,4]], ('w1','w2','path')]
df2.loc[0:5, ('w1','w2','path')]    

df2.loc[df2.index[[0,1,2,3,4]], ('w1','w2')]
df2.loc[0:5, ('w1','w2')]    

for i in range(len(df2)):
    df2.loc[df2.index[[i]], 'path'] = i+5

print(df2)
    
#%%

df = pd.read_csv("~/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/data/ws353.tsv", sep='\t',
                 header=None,
                 names=['w1', 'w2', 'judgement'])

names = ['path', 'lch', 'wup', 'res', 'jcn','lin']

for name in names:
    df[name] = None
    df[name+'.cov'] = None

# print(df.columns)
# print(df.head())

wordnet_ic = WordNetInformationContent(corpus='bnc', resnik=True, add1=True) # taken from README on github
# is there another corpus that I could use to calculate IC?

for i in range(len(df)):
    w1 = df.loc[df.index[[i]], 'w1'].to_string(index=False).strip()
    w2 = df.loc[df.index[[i]], 'w2'].to_string(index=False).strip()

    w1_synset = wordnet.synsets(w1)[0]
    w2_synset = wordnet.synsets(w2)[0]
    
    try:
        df.loc[df.index[[i]], 'path'] = round(wordnet.path_similarity(w1_synset, w2_synset), 4) # path similarity
        df.loc[df.index[[i]], 'path.cov'] = 1
    except (NameError, TypeError, WordNetError):
        df.loc[df.index[[i]], 'path'] = None
        df.loc[df.index[[i]], 'path.cov'] = 0
        
    try:
        df.loc[df.index[[i]], 'lch'] = round(wordnet.lch_similarity(w1_synset, w2_synset), 4) # Leacock-Chodorow similarity
        df.loc[df.index[[i]], 'lch.cov'] = 1
    except (NameError, TypeError, WordNetError):
        df.loc[df.index[[i]], 'lch'] = None
        df.loc[df.index[[i]], 'lch.cov'] = 0
        
    try:
        df.loc[df.index[[i]], 'wup'] = round(wordnet.wup_similarity(w1_synset, w2_synset), 4) # Wu-Palmer similarity
        df.loc[df.index[[i]], 'wup.cov'] = 1
    except (NameError, TypeError, WordNetError):
        df.loc[df.index[[i]], 'wup'] = None
        df.loc[df.index[[i]], 'wup.cov'] = 0
        
    try:
        df.loc[df.index[[i]], 'res'] = round(wordnet.res_similarity(w1_synset, w2_synset, wordnet_ic), 4) # Resnik similarity,
        df.loc[df.index[[i]], 'res.cov'] = 1
    except (NameError, TypeError, WordNetError):
        df.loc[df.index[[i]], 'res'] = None
        df.loc[df.index[[i]], 'res.cov'] = 0
        
    try:
        df.loc[df.index[[i]], 'jcn'] = round(wordnet.jcn_similarity(w1_synset, w2_synset, wordnet_ic), 4) # Jiang-Conrath similarity
        df.loc[df.index[[i]], 'jcn.cov'] = 1
    except (NameError, TypeError, WordNetError):
        df.loc[df.index[[i]], 'jcn'] = None
        df.loc[df.index[[i]], 'jcn.cov'] = 0

    try:
        df.loc[df.index[[i]], 'lin'] = round(wordnet.lin_similarity(w1_synset, w2_synset, wordnet_ic), 4) # Lin similarity
        df.loc[df.index[[i]], 'lin.cov'] = 1
    except (NameError, TypeError, WordNetError):
        df.loc[df.index[[i]], 'lin'] = None
        df.loc[df.index[[i]], 'lin.cov'] = 0

df.to_csv('~/Dropbox/CUNY/Language_Technology/labs/lab1-lowrycb/part1_wordnet.tsv', sep='\t')

#%%

for name in names:
    df2 = df.loc[:,('judgement',name)] # selecting two columns
    df2 = df2[df2[name].notnull()] # removing None values
    x = stats.spearmanr(df2['judgement'], df2[name])
    print(f"""For human judgements and {name} similarity, the Spearman's rho is {round(x[0],3)} 
    with p-value of {round(x[1],3)} \n""")

for name in names:
    coverage = df[name+".cov"]
    x = sum(coverage) 
    y = x / len(coverage)
    print(f"The coverage of {name} similarity is {x} words, {round(y,2)}% of the data.\n")
