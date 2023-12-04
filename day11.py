#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass_sum(arr, row, col):
    # Calculate the sum of the hourglass
    return (
        arr[row][col] + arr[row][col + 1] + arr[row][col + 2] +
        arr[row + 1][col + 1] +
        arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
    )

def max_hourglass_sum(arr):
    max_sum = float('-inf')  # Initialize to negative infinity

    for row in range(4):
        for col in range(4):
            current_sum = hourglass_sum(arr, row, col)
            max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == '__main__':
    # Read the 6x6 array from input
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Calculate and print the maximum hourglass sum
    result = max_hourglass_sum(arr)
    print(result)
