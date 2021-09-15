# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:08:06 2021

@author: LG
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)


kfold = KFold(n_splits=5)
cv_accuracy = []

# In[1]

n_iter = 0

for train_index, test_index in kfold.split(features):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index],label[test_index]
    
    
    dt_clf.fit(X_train,y_train)
    pred = dt_clf.predict(X_test)
    n_iter += 1
    accruacy = np.round(accuracy_score(y_test,pred),4)
    
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    
    cv_accuracy.append(accruacy)
    
# In[2]

print(np.mean(cv_accuracy))







