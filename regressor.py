# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:56:52 2015

@author: dmitry
"""

from sklearn.tree import DecisionTreeRegressor
from sklearn.base import BaseEstimator

class Regressor(BaseEstimator):
    def __init__(self):
        self.clf = DecisionTreeRegressor(max_depth=5)

    def fit(self, X, y):
        self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict(X)

