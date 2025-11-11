# recursive exponent question

def exponent(base,exp):
    if exp == 0: 
        return 1
    elif exp == 1: 
        return base
    else: 
        return base * exponent(base, exp - 1)


