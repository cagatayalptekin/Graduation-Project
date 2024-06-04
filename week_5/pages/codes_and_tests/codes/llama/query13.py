import math

# def prime_factors(n):
#     # base case: if n = 1, return [1]
#     if n == 1:
#         return [1]

#     # otherwise, find the GCD of n and 1
#     gcd = math.gcd(n, 1)

#     # divide n by the GCD to find the prime factors
#     factors = []
#     while n != 1:
#         factors.append(gcd)
#         n = n // gcd
#     return factors

def prime_factors(n):
    if n == 1 or n == 0:
        return [1]
    else:
        gcd = math.gcd(n, 1)
        factors = []
        while n != 0:
            factor = n // gcd
            factors.append(factor)
            n -= factor * gcd
        return factors + [n]

# def prime_factors(n):
#     if n == 1 or n == 0:
#         return [1]
#     else:
#         factors = []
#         gcd, rest = math.gcd(n, 1)
#         while rest != 0:
#             factors.append(rest)
#             gcd, rest = math.gcd(rest, gcd)
#         return factors + [n // gcd]