# -*- coding: utf-8 -*-
"""FakeNewsDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qlIHELe5Qnft9CoNjYG0rNOuyaHjwH11
"""

import pandas as pd
import numpy as np

from google.colab import files
uploaded = files.upload()
fake = pd.read_csv('data.csv')

fake.head()

fake = fake.drop(['URLs'], axis = 1)
fake = fake.dropna()

fake.head()

fake = fake[0:1000]

X = fake.iloc[:,:-1].values
y = fake.iloc[:,-1].values

X[0]

y[0]

from sklearn.feature_extractiom.text import CountVectorize
cv = CountVectorize(max_features = 5000)
mat_body = cv.fit_transform(X[:,1]).todense()

mat_body

cv_head = CountVectorize(max_features = 5000)
mat_head = cv_head.fit_transform(X[:,0]).todense()

mat_head

X_mat = np.hstack((mat_head, mat_body))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_mat, y, test_size = 2, random_state = 0)

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = 'entropy')
dtc.fit(X_train, y_train)
dtc.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred_dtr)

