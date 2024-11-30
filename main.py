#importing matplolib
import matplotlib.pyplot as plt
#importing seaborn
import seaborn as sns
#importing pandas
import pandas as pd
#importing numpy
import numpy as np
#reading dataframe
df=pd.read_csv("ti.csv")
print(df.head())
#checking for null values
df.isnull().any()
#
#
#finding passengers from which gender who survived the most
sns.countplot(df,x='Gender',hue='Survived')
plt.show()
#
#
sns.set_style('darkgrid')
sns.countplot(df,x='Pclass',hue='Survived')
plt.show()
#
#creating a dis plot
sns.histplot(df['Age'],bins=40)
plt.show()
sns.displot(df['Fare'])
plt.show()
#
sns.heatmap(df.corr())
plt.show()