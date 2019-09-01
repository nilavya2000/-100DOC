#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
#Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#for example,ar=[1,3,5,7,9] . Our minimum sum is 1+3+5+7= 16 and our maximum sum is 3+5+7+9=24. We would print 16 24
#nput Format

#A single line of five space-separated integers.

#Output Format

#Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    s=[5]
    a=0
    for i in s:
        sum=0
        for j in arr:
            if j==i:
                a+=1
            else:
                sum+=arr[j]
        s[i]=sum
    min=s[0]
    max=s[0]
    for i in range(1,5):
        if min>s[i]:
            min=s[i]
        if max<s[i]:
            max=s[i]
    print(min, " ",max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
