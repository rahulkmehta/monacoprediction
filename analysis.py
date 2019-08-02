import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter

raceFrame = pd.read_csv("data/normalized_race_data.csv")
print (raceFrame.head())

print ("DROPPING NAMES")
raceFrame = raceFrame.drop(['name', 'year'], 1)
print (raceFrame.head())

print ("SHOWING CORRELATIONS")
print (raceFrame.corr())

plt.scatter(raceFrame['normalized'], raceFrame['finalposition'])
plt.show()

raceFrame = raceFrame.reset_index()

raceFrame_data = raceFrame.ix[:,(0,1,2,3,4)].values
raceFrame_target = raceFrame.ix[:,6].values

raceFrame_data_names = ['qualiposition','qone','qtwo','qthree','normalized']
X,y = scale(raceFrame_data), raceFrame_target

print ("CHECKING FOR MISSING VALUES")
missing_values = X == np.NAN
X[missing_values == True]
print ("NONE FOUND")

print(np.any(np.isnan(X)))
print(np.all(np.isfinite(X)))

LinReg = LinearRegression(normalize = True)
LinReg.fit(X,y)

print (LinReg.score(X,y))
