import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Titanic Dataset.csv')
print(df.head())

mean_age=np.mean(df['Age'])         
print('Mean age of passengers is',mean_age)

mean_fare=np.mean(df['Fare'])         
print('Mean fare is',mean_fare)