import pandas as pd

df = pd.read_csv('D:\Study\Correlation-analysis\Diabetes.csv')

pd.set_option('display.max_rows', 140)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width',600)
print(df.head())

df=df.sample(n=50)

from pandas.plotting import scatter_matrix
df1=pd.DataFrame(df)
scatter_matrix(df1, alpha = 1, figsize = (25, 25), diagonal="kde")

df.corr()

import matplotlib.pyplot as plt

f = plt.figure(figsize=(15, 15))
plt.matshow(df.corr(), fignum=f.number)
plt.xticks(range(df.shape[1]), df.columns, fontsize=14, rotation=45)
plt.yticks(range(df.shape[1]), df.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16);

from scipy.stats import spearmanr
corr1, _ = spearmanr(df['Age'], df['Pregnancies'])
corr2, _ = spearmanr(df['Insulin'], df['SkinThickness'])
corr3, _ = spearmanr(df['BMI'], df['SkinThickness'])
print('Spearmans  correlation: %.3f' % corr1)
print('Spearmans  correlation: %.3f' % corr2)
print('Spearmans  correlation: %.3f' % corr3)

from math import *
t1=corr1/sqrt(1/49)
print(t1)
t2=corr2/sqrt(1/49)
print(t2)
t3=corr3/sqrt(1/49)
print(t3)

if(t1>2.576):
 print("H0 - corr=0 Is not correct => correlation coef is statistically valuable")
if(t2>2.576):
 print("H0 - corr=0 Is not correct => correlation coef is statistically valuable")
if(t3>2.576):
 print("H0 - corr=0 Is not correct => correlation coef is statistically valuable")


from scipy.stats import pearsonr
corr1, _ = pearsonr(df['Age'], df['Pregnancies'])
corr2, _ = pearsonr(df['Insulin'], df['SkinThickness'])
corr3, _ = pearsonr(df['BMI'], df['SkinThickness'])
print('Pearsons correlation: %.3f' % corr1)
print('Pearsons correlation: %.3f' % corr2)
print('Pearsons correlation: %.3f' % corr3)

from math import *
t1=corr1*sqrt(50-2)/sqrt(1-corr1**2)
print(t1)
t2=corr2*sqrt(50-2)/sqrt(1-corr2**2)
print(t2)
t3=corr3*sqrt(50-2)/sqrt(1-corr3**2)
print(t3)


if(t1>2.576):
 print("H0 - corr=0 Is not correct => correlation coef is statistically valuable")
if(t2>2.576):
 print("H0 - corr=0 Is not correct => correlation coef is statistically valuable")
if(t3>2.576):
 print("H0 - corr=0 Is not correct => correlation coef is statistically valuable")