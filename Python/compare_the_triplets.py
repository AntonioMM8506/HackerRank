import math
import os
import random
import re
import sys 

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    #in order to read the maps, first we have to translate them as lists.
    a1 = list(a)
    b1 = list(b)
    
    res = [0,0]

    for i in range(len(a1)):
        if(a1[i]>b1[i]):
            res[0]+=1
        elif (a1[i]<b1[i]):
            res[1]+=1
    
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #In case there's an error when running in an IDE, change the line for
    #what is below
    fptr = sys.stdout

    a = map(int, input().rstrip().split())
    b = map(int, input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
