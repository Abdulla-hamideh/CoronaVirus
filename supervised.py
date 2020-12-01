import numpy as np
import pandas as pd
from sklearn import cluster
from sklearn import metrics
from sklearn.preprocessing import scale
from sklearn import cluster
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('always')  # "error", "ignore", "always", "default", "module" or "once"


data = pd.read_csv("trend_ca_20201026.csv")
data[data["DailyPositive"] != 0]
data[data["DailyDeaths"] != 0]
data[data["CumulativeDeaths"] != 0]
data[data["CumulativePositive"] != 0]
print(data)

X = data.values[:, 1:6]
Y = data.values[:, 0]
Y=Y.astype('int')

from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y,test_size = 0.5)
print("LOGISTIC REGRESSION")
print("**************************************")
lm = LogisticRegression(max_iter= 1200000)
lm.fit(X_train, Y_train)
lm.predict_proba(X_test)
predicted = lm.predict(X_test)
print(metrics.classification_report(Y_test, predicted))
print(metrics.confusion_matrix(Y_test, predicted))

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(weights= "distance")
model.fit(X_train, Y_train)
print(model)
predicted = model.predict(X_test)
print(metrics.classification_report(Y_test, predicted))
print(metrics.confusion_matrix(Y_test, predicted))

