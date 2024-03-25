#query_3="Write a function that takes two integers as input and finds their greatest common divisor."




def gcd_codellama(a, b):
    if b == 0:
        return a
    else:
        return gcd_codellama(b, a % b)
    

def gcd_llama(a, b):
    if b == 0:
        return a
    else:
        return gcd_llama(b, a % b)


def gcd_mistral(a, b):
    while b != 0:
        a, b = b, a % b
    return a

