import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


y_pred = np.array([0.9, 0.2, 0.1, 0.4, 0.9])
y_ans = np.array([1, 0, 0, 1, 1])


def l1_norm(y_pred_f, y_ans_f):
    ans = 0
    for i in range(len(y_pred_f)):
        ans += abs(y_ans_f[i] - y_pred_f[i])
    return ans


def l2_norm(y_pred_f, y_ans_f):
    ans = 0
    for i in range(len(y_pred_f)):
        ans += (y_ans_f[i] - y_pred_f[i]) ** 2
    return ans


def non_unique(x):
    ans = np.array([])
    rows, columns = x.shape
    for line in range(rows):
        eq = True
        element = x[line, 0]
        for ind in range(1, len(x[line])):
            if element != x[line, ind]:
                eq = False
                break
        if eq:
            ans = np.append(ans, x[line])
    ans = np.reshape(ans, (ans.size // columns, columns))
    return ans
