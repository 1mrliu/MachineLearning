# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/7/7 5:07 PM'
import mglearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

# load data an split data
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
print(X_train)

# compute the minimum and maximum on the train data
scaler = MinMaxScaler().fit(X_train)

# rescale the training data
X_train_scaled = scaler.transform(X_train)

svm = SVC()
# learn an svm on the scaled training data
svm.fit(X_train_scaled, y_train)
X_test_scaled = scaler.transform(X_test)
print("Test score: {:.2f}".format(svm.score(X_test_scaled, y_test)))


# GridSearchCV for the proper parameter
param_grids = {'C' : [0.001, 0.01, 0.1, 1, 10, 100], 'gamma' : [0.001, 0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(SVC(), param_grid=param_grids, cv=5)
grid.fit(X_train_scaled, y_train)
print("Best cross-validation accuracy: {:.2f}".format(grid.best_score_))
print("Best set score: {:.2f}".format(grid.score(X_test_scaled, y_test)))
print("Best parameter: ", grid.best_params_)
mglearn.plots.plot_improper_processing()
pipe = Pipeline([("scaler", MinMaxScaler()),("svm", SVC())])
pipe.fit(X_train, y_train)
print("Pipe Test score:{:.2f}".format(pipe.score(X_test, y_test)))
