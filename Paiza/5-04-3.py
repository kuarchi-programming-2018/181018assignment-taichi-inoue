# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:55:09 2018

@author: Inoue
"""


points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0

for key in points:
    sum += points[key]
print(int(sum))