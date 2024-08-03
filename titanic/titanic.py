import os
import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv("titanic/train.csv")
df_test = pd.read_csv("titanic/test.csv")

df_train.head()

fig, ax = plt.subplots()
ax.plot(df_train.Fare, df_train.Survived)
plt.show()