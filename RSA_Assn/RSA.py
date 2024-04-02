# BJC, Original Author
# 4/1/2024

# RSA Class for encryption assignment

class RSA:

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def generate_keys(self):
        while True:
            string1 = input("Please enter first string: ")
            string2 = input("Please enter second string: ")
            p = self.to_base_10(string1)
            q = self.to_base_10(string2)
            if p >= 10**200 and q >= 10**200:
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


text1 = "verylongtextstring1"
text2 = "anotherverylongtextstring2"

rsa_instance = RSA()
p, q = rsa_instance.generate_keys()
print("p:", p)
print("q:", q)
