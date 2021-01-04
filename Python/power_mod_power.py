def pow_mod_pow(a,b,m):
    #m can not be a negative number
    if(m<=0):
        print("m can not be a negative number")
        return False 
    
    power = a**b
    power_mod = pow(a,b,m)

    print(power)
    print(power_mod)


if __name__ == '__main__':
    #Given the 3 parameters, the function can proceed. 
    #a and b can be any real number. 
    a = int(input())
    b = int(input())
    m = int(input())

    pow_mod_pow(a,b,m)
