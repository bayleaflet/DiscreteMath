#BJC, Original Author, 2/9/24
# Uses Miller's test to determine if a number is prime
import random

def is_prime_miller(N, loop_num):
    for i in range(loop_num):
        b = random.randrange(2,n)
        OK = miller_test(n,b)
        if not OK:
            return False # Not a Primer Number, is compositie
    return True

def miller_test(n,b):
    t = n-1
    s = 0
    if pow(b,t,n) = 1:
        return True
    for loop in range(s):
        # Insert the 5 conditions
        # if they pass, return True

    #If they all fail,
    return False # The result is composite
