def calculate_hcf(x, y):  
    # selecting the smaller number  
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf

def GCD(a, b):
    if(b == 0):
        return abs(a)
    else:
        return GCD(b, a % b)

