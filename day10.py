#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    count=0
    maxCount=0
    binary=bin(n)
    #Removing the 'ob' prefix
    OnlyBinary=binary[2:]
    print(OnlyBinary)
    for i in OnlyBinary:
        if i=='1':
            count+=1
            maxCount=max(count,maxCount)
        else:
            count=0
        
    print(maxCount)
            
