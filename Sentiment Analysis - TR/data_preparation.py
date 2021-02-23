# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:22:53 2020

@author: ozcan
"""
import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\ozcan\Desktop\Özcan Gündeş\Yüksek Lisans BOUN\583\Assignment2\yorumsentiment.csv",encoding="utf-8")
df=df.drop(columns=["Unnamed: 0"],axis=1)
df.head()
df.rating.value_counts()
#make ternary--> 0 means negative, 1 means neutral and 2 means positive
df['label'] = np.where((df.rating == 1) | (df.rating == 2), 0, np.where((df.rating == 4) | (df.rating == 5),2,1))
df=df.rename(columns={"comment":"review"})
df=df[["review","label"]]
df.label.value_counts()


from sklearn.model_selection import train_test_split
df_train, df_test, y_train, y_valid = train_test_split(df, df["label"], test_size=0.25, random_state=0)

df_train=df_train.reset_index(drop=True)

df_test=df_test.reset_index(drop=True)

df_train.label.value_counts()
df_test.label.value_counts()

df_train=df_train.groupby('label').apply(lambda x: x.sample(n=2350,random_state=1)).reset_index(drop=True)
df_test=df_test.groupby('label').apply(lambda x: x.sample(n=800,random_state=1)).reset_index(drop=True)

df_train.to_csv(r'C:\Users\ozcan\Desktop\NLP Scripts\Compec Workshop\kitapyurdu\train.csv')
df_test.to_csv(r'C:\Users\ozcan\Desktop\NLP Scripts\Compec Workshop\kitapyurdu\test.csv')
