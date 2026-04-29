import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stats

df=pd.read_csv('Titanic Dataset.csv')
print(df.head())

median_age=np.median(df['Age'])
print('Median age of passengers is',median_age)

median_fare=np.median(df['Fare'])
print('Median fare is',median_fare)

mode_age=stats.mode(df['Age'])
print('Mode age of passengers is',mode_age)

mode_class=stats.mode(df['Pclass'])
print('Mode class of passengers is',mode_class)

mode_gender=df['Gender'].value_counts().index[0]
print('Mode of feature gender',mode_gender)

mode_embarked=df['Embarked'].value_counts().index[0]
print('Mode of feature embarked',mode_embarked)