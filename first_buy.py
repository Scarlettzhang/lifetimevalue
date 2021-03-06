# Estimate the likelihood of a user becoming a profitible user in 30 days based on the features of the first lot bought.

import numpy as np
import h5py
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm


rawData = pd.read_csv('sku_ltv.csv')
dx = rawData.iloc[:,1:9]
dy = rawData.iloc[:,9]


X_train, X_test, y_train, y_test = train_test_split(dx, dy, test_size = 0.4)
X_train = X_train.values
X_test = X_test.values
y_train = y_train.values
y_test = y_test.values


clf = svm.SVC(C=0.6, kernel='rbf')
clf.fit(X_train,y_train)
p = clf.predict(X_test)
m = len(y_test)

print("Accuracy: "  + str(np.sum((p == y_test))/m))
