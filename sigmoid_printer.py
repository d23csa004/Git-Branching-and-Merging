# -*- coding: utf-8 -*-
"""sigmoid_printer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EClwdTx_XFS5YY2yNpWIECb82S0I-cwN
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

print("Sigmoid values for random data:")
for value in random_values:
    print(f"Sigmoid({value}) = {sigmoid(value)}")