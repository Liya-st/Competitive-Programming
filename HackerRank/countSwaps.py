#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    isSorted= False
    count = 0 
    for i in range(len(a)):
        while not isSorted:
            isSorted = True
            if(a[i-1]< a[i]):
                isSorted = False
                count +=1
                a[i-1], a[i] = a[i], a[i-1]
    print(f"Array is sorted in {count} swaps.")
    print ("First Element:" ,  a[0])
    print ("Last Element: ", a[-1])

    


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
