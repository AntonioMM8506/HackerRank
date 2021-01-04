#from __future__ import print_function

if __name__ == '__main__':
    n = int(input())

    #In a list, stores all the the consecutive values until the given value
    #in a tring format
    list_1 = []
    for i in range(n):
        list_1.append(str(i+1))
    
    #Then, with join, concatenates all the numbers as a single string with
    #no spaces
    str1 = ''.join(list_1)
    print(str1)
    
