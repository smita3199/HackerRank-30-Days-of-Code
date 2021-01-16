#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        data = input().split()
        name = data[0]
        email = data[1]
        match = re.search(r'[\w\.-]+@gmail.com', email)
        if match:
            arr.append(name)
    arr.sort()
    for name in arr:
        print(name)
