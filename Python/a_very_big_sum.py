import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    ar_aux = list(ar)
    res =  sum(ar_aux)
    return res    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = map(int, input().rstrip().split())

    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
