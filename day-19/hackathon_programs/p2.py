#Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
#Print the decimal value of each fraction on a new line.


import math
import os
import random
import re
import sys


def plusMinus(arr,i):
    c=0
    d=0
    e=0
    for n in arr:
        if n>0:
            c+=1
        elif n<0:
            d+=1
        else:
            e+=1
    print(float(c/i))
    print(float(d/i))
    print(float(e/i))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)

