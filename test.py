#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: smx
# @Date  : 2020/2/28
# @Desc  :

from sklearn.datasets import make_regression

reg_data, reg_target = make_regression(n_samples=200, n_features=1500, n_informative=3, noise=7)

from sklearn.linear_model import LogisticRegression

target = [int(each) for each in reg_target]

lasso = LogisticRegression()
lasso.fit(reg_data, target)
pred = lasso.predict(reg_data)

set1 = set(target)
set2 = set(pred)
print(len(set1), len(set2), len(set1 and set2))
