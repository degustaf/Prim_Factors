################################################################################
# Project Euler Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
################################################################################

from math import sqrt, floor

def seive(N):
    result = []
    limit = floor(sqrt(N + 1))
    number_list = [True] * (N+1)
    number_list[0] = False
    number_list[1] = False

    for index in range(2, limit):
        if not number_list[index]:
            continue
        for multiple in range(2 * index, N + 1, index):
            number_list[multiple] = False

    result = []
    for index, val in enumerate(number_list):
        if val:
            result.append(index)

    return result

def largest_prime_factor(N):
    primes = seive(floor(sqrt(N + 1)))

    residual = N
    for factor in primes:
        quotient, remainder = divmod(residual, factor)
        while remainder == 0 and quotient != 1:
            residual = quotient
            quotient, remainder = divmod(residual, factor)

        if quotient == 1 and remainder == 0:
            return factor

    return residual

if __name__ == "__main__":
    result = largest_prime_factor(100)
    print(result)

    result = largest_prime_factor(13195)
    print(result)
    
    result = largest_prime_factor(600851475143)
    print(result)
