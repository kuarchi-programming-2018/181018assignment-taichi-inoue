# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:16:15 2018

@author: Inoue
"""

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    
    def sum(self):
        return self.kokugo + self.sansu

yamada = Gakusei(70, 43)
print("合計は" + str(yamada.sum()) + "点です")