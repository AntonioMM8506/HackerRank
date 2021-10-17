#Function 
def input_data(a,b,c,d): 
    pow_1 = a**b
    pow_2 = c**d
    res = pow_1 + pow_2

    print(res)

#Main
if __name__ == "__main__":
    #Recieves the 4 parameters as input data and then uses them
    #in the function above.
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    input_data(a, b, c, d)