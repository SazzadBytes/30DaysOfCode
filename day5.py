#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        mul=n*i
        print(str(n)+" x "+str(i)+" = "+str(mul))
        i=i+1
