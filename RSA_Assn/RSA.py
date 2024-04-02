# BJC, Original Author
# 4/1/2024

# RSA Class for encryption assignment

class RSA:

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def generate_keys(self, string1, string2):
        p = self.to_base_10(string1)
        q = self.to_base_10(string2)
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
p, q = rsa_instance.generate_keys(text1,text2)
print("p:", p)
print("q:", q)
