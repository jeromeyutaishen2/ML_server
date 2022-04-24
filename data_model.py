# -*- coding: utf-8 -*-
"""
Created on Apr 23 16:12:51 2022

@author: Jerome Yutai Shen

"""


from sklearn import svm
import joblib
from default_settings import MODEL_FILENAME
from os.path import exists as os_path_exists
import pandas as pd
import numpy as np


def train_model(X_train, y_train):
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    return clf


def save_model(clf):
    joblib.dump(clf, MODEL_FILENAME)


def load_saved_model():
    if os_path_exists(MODEL_FILENAME):
        return joblib.load(MODEL_FILENAME)
    else:
        return os_path_exists(MODEL_FILENAME)


def pandas_csvreader(filename: str):
    return pd.read_csv(filename)


def string2array(values_char: str):
    return np.reshape(np.fromstring(values_char, sep = ","), (1, -1))





