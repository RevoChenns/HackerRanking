import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
while True:
    if 1 <= n <= 100:
        # Input satisfies the constraint, break the loop
        break
    else:
        print("Input must be between 1 and 10.")
        
if  n % 2 == 1 or (n % 2 == 0 and 6<n<20):
    print('Weird')
if (n % 2 == 0 and 2<n<5) or 20<n:
    print('Not Weird')