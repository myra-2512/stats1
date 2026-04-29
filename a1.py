import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=pd.read_csv('Titanic Dataset.csv')
print(df.head(5))

print(df.dtypes)

print(df.isnull().sum())