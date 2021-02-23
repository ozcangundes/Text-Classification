# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:50:49 2020

@author: ozcan
"""

file = open(r'C:\Users\ozcan\Desktop\NLP Scripts\Compec Workshop\Musical_Instruments_5\Musical_Instruments_5.json',"r")

final_dict=[]
totalLinesInInputFile=0

true=True
false=False
for line in file:
    lineDictionary=eval(line)
    final_dict.append(lineDictionary)
    totalLinesInInputFile+=1

import pandas as pd
import numpy as np
df=pd.DataFrame(final_dict)

df=df[["reviewText","overall"]]
df=df.rename(columns={"reviewText":"review","overall":"label"})

df.label.value_counts()

df['label'] = np.where((df.label == 1) | (df.label == 2), 0, np.where((df.label == 4) | (df.label == 5),2,1))

from sklearn.model_selection import train_test_split
df_train, df_test, y_train, y_valid = train_test_split(df, df["label"], test_size=0.25, random_state=0)

df_train.label.value_counts()
df_test.label.value_counts()

df_train.