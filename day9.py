import math
import os
import random
import re
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        mul = 1
        for i in range(1, n + 1):
            mul *= i
        return mul

if __name__ == '__main__':
    n = int(input().strip())
    result = factorial(n)
    print(result)