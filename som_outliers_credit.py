# -*- coding: utf-8 -*-
"""SOM - Outliers - Credit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vt1wiMvGFpqXhWkWr7xQx8-oXXtspBf0
"""

!pip install minisom

import minisom
import pandas as dpd
import sklearn
import matplotlib
import numpy as np

pd.__version__, sklearn.pd__version__, matplotlib.__version__, np.__version__

from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler
from matplotlib.pylab import pcolor, colorbar, plot

dataset = pd.read_csv('credit_data.csv')

dataset.isna().sum
dataset = dataset.dropna()

dataset.loc[dataset['age']<0]

dataset['age'].mean()

dataset.loc[datset['age']>0].mean()

mean_age = dataset.loc[dataset['age'] > 0, 'age'].mean()
dataset.loc[dataset['age'] < 0, 'age'] = mean_age

X = dataset.iloc[:, 0:4].values

y = dataset.iloc[:, 4].values

normalize = MinMaxScaler(feature_range=(0,1))
X = normalize.fit_transform(X)

som = MiniSom(x = 15 , y = 15, input_len=4, random_seed=0)
som.random_weights_init(X)
som.train_random(data=X, num_iteration=100)

pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x enumerate(X):
  w = som.winner(x)
  plot(w[0]  + 0.5, w[1] + 0.5, markers[int(y[i])], markerfacolor = 'None', markersize = 10, markeredgecolor=colors[y[i]], markeredgewidth=2)

map = som.win_map(X)

susp = np.concatenate((map[(5,4)], map[(13,6)]), axis=0)

susp = normalizer.inverse_transform(susp)

class_ = []
for i in range(len(dataset)):
  for j in range(len(susp)):
    if dataset.iloc[i,0] == int(round(susp[j,0])):
      classe.append(dataset.iloc[i,4])
class_ = np.asarray(class_)

susp_final = np.column_stack((sus, class_))
susp_final = susp_final[susp_final[:, 4].argsort()]

susp_final[:,0] = np.round(susp_final[:,0]).astype(int)