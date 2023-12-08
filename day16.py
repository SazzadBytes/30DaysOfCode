#!/bin/python3

import math
import os
import random
import re
import sys


S = input().strip()
try:
  convert_int=int(S)
  print(convert_int)
except ValueError:
  print("Bad String")    
