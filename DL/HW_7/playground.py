import numpy as np
import pandas as pd


df1 = pd.read_csv("../../data/titanic_data.csv", index_col="PassengerId")
# print(df1.head())
# print(df1.columns)

# sex = df1['Sex']
# print(sex.value_counts())

# cl = df1['Pclass']
# print(cl.value_counts())

# age = df1['Age']
# print(age.min(), age.max(), age.mean())

# grcls = df1.groupby('Pclass')
# print(grcls['Age'].mean())

df2 = pd.read_csv("../../data/titanic_surv.csv")
df2.index = np.arange(1, 892)
# print(df2.tail(10))
# print(df2.sample(frac=1))

joined = df1.join(other=df2)
# print(joined)

# total survived
print("total survived", joined["Survived"].value_counts().get(1))

# survived by 'Sex'
print("by Sex", joined.groupby(["Sex"])['Survived'].sum())

# correlation by Survived, Sex, Age
corr_data = joined[['Survived', 'Sex', 'Age']]
corr_data['Sex'] = (corr_data['Sex'] == "female").astype(dtype=int)
print(corr_data.corr())
