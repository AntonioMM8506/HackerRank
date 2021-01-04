#!/bin/python

from __future__ import print_function

import os
import sys

#@param recieves a map as an argument
#@return the sum of all the numbers inside the map.
def simpleArraySum(ar):
    ar_1 = list(ar)
    total = 0
    for i in ar_1:
        total += i
    
    return total
#End of simpleArraySum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = map(int, input().rstrip().split())
    #print(list(ar))
    
    result = simpleArraySum(ar)
    print(result)

    fptr.write(str(result) + '\n')
    fptr.close()
