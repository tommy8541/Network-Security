# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:31:05 2019

@author: Lab611
"""

import sys
import math
import random as rd

SIZE = 100000
SIZE2 = 300000
MAX = 8000000
MAX2 = 10000000
primes = []
nbPrimes = -1

def genPrimes(SIZE):
    n = 0
    mark = []
    for i in range(SIZE):
        mark.append(0)
    for i in range(2, SIZE):
        if mark[i] == 0:
            n += 1
            for j in range(i + i, SIZE, i):
                mark[j] = 1
    # save primes list
    for i in range(2, len(mark)):
        if mark[i] == 0:
            primes.append(i)
            
    print ('primes')
    return n, primes