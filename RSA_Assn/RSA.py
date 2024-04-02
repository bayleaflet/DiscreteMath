# BJC, Original Author
# 4/1/2024

# RSA Class for encryption assignment
import miller_alg

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



rsa_instance = RSA()
p, q = rsa_instance.generate_keys()
print("p:", p)
print("q:", q)
