#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    total_swap=0
    a = list(map(int, input().rstrip().split()))
    for i in range(n):
        for j in range(n-1):
            
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                total_swap+=1
    print("Array is sorted in",total_swap,"swaps")
    print("First Element:",a[0])
    print("Last Element:",a[-1])

    
