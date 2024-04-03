# BJC, Original Author
# 4/1/2024

# RSA Class for encryption assignment
import miller_alg
import math

class RSA:

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def generate_keys(self):
        while True:
            string1 = input("Please enter first string: ")
            string2 = input("Please enter second string: ")
            p = self.to_base_10(string1)
            q = self.to_base_10(string2)
            # Commented out below for easier way of testing, will re-initiate
            # if p >= 10**200 and q >= 10**200:
            if p >= 20 and q >= 20:
                break
            else:
                print("Your input strings are too short. Try again.")
                continue
        p = p % 10 ** 200 # Mod so they aren't too long
        q = q % 10 ** 200
        # Make sure p and q are odd
        if p % 2 == 0:
            p += 1
        if q % 2 == 0:
            q += 1
        # Pass in p and q into millers algorithm
        # If miller's returns True, answer is a probable prime
        while True:
            if not miller_alg.main(p): # If millers algorithm returns False
            # Number is definitely composite. Continue loop.
                p += 2
                continue
            if not miller_alg.main(q):
                q += 2
                continue
            break
        n = p * q
        r = (p-1)*(q-1)

        # find e -> a 398 digit number relatively prim with r
        # Commenting out this, will swap in later

        # e = 10**398 + 1
        e = 10**39 + 1
        while True:
            if math.gcd(e,r) == 1:
                break
            e += 1

        # find d -> the inverse of e mod r
        d = inverse(e,r)

        # Write n and e to public.txt
        with open("public.txt", "w") as file:
            file.write(str(n) + "\n")
            file.write(str(e) + "\n")

        # Write n and d to private.txt
        with open("private.txt", "w") as file:
            file.write(str(n) + "\n")
            file.write(str(d) + "\n")

        return p, q

    def encrypt(self, input_file, output_file):
        pass

    def decrypt(self, input_file, output_file):
        pass

    def to_base_10(self, text):
        base = len(self.alphabet)
        answer = 0
        for c in text:
            if c in self.alphabet:
                answer = answer * base + self.alphabet.index(c)
        return answer

def inverse(a,n):
    t, newt = 0,1
    r, newr = n, a

    while newr != 0:
        quotient = r//newr
        t, newt = newt, t-quotient * newt
        r, newr = newr, r - quotient * newr

    if r> 1:
        return "a is not invertible"

    if t < 0:
        t += n
    return t

