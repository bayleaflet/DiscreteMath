# BJC, Original Author, 2/9/24
# Uses Miller's test to determine if a number is prime
import random

def is_prime_miller(N, loop_num):
    for i in range(loop_num):
        b = random.randrange(2,N)
        OK = miller_test(N,b)
        if not OK:
            return False # Not a Primer Number, is compositie
    return True

def miller_test(n,b):
    t = n-1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1

    if pow(b,t,n) == 1:
        return True

    for loop in range(s):
        if pow(b, 2**loop *t, n) == n - 1:
            return True
        elif pow(b, 2**loop * t, n) == 1:
            continue # Try Next iteration, don't return false yet
        # if they pass, return True

    #If they all fail,
    return False # The result is composite

def main(infix):

    # infix = int(input("Enter number here to test if prime: "))
    loop_num = 40
    result = is_prime_miller(infix, loop_num)
    if result:
        # Later we will adjust this to return True if prime
        return True
        # print("Your number is a probable prime, and is only divisble by itself and 1.")
    else:
        # Later we will adjust this to return False when not prime
        return False
        # print("Your number is composite.")

if __name__ == "__main__":
    main()
