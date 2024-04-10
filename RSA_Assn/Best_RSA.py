import miller_alg
import math

class RSA:

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.encrypt_alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.block_size = math.ceil(math.log(10**400, len(self.encrypt_alphabet)))

    def generate_keys(self):
        while True:
            string1 = input("Please enter first string: ")
            string2 = input("Please enter second string: ")
            p = self.to_base_10(string1, self.alphabet)
            q = self.to_base_10(string2, self.alphabet)

            if p >= 200 and q >= 200:
                break
            else:
                print("Your input strings are too short. Try again.")
                continue

        p = p % 10 ** 200  # Mod so they aren't too long
        q = q % 10 ** 200
        # Make sure p and q are odd
        if p % 2 == 0:
            p += 1
        if q % 2 == 0:
            q += 1

        # Pass in p and q into Miller's algorithm
        # If Miller's returns True, answer is a probable prime
        while True:
            if not miller_alg.main(p):  # If Miller's algorithm returns False
                # Number is definitely composite. Continue loop.
                p += 2
                continue
            if not miller_alg.main(q):
                q += 2
                continue
            break

        n = p * q
        r = (p - 1) * (q - 1)

        # find e -> a 398 digit number relatively prime with r
        e = 65537  # Recommended public exponent
        while True:
            if math.gcd(e, r) == 1:
                break
            e += 1

        # find d -> the inverse of e mod r
        d = self.inverse(e, r)

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
        # Open input file in binary mode, read contents
        with open(input_file, "rb") as fin:
            plain_text_binary = fin.read()

        # Decode binary data into a Unicode str using UTF-8 encoding
        plain_text = plain_text_binary.decode("utf-8")

        # Breaks down plaintext into blocks no bigger than block_size
        blocks = [plain_text[i:i + self.block_size] for i in range(0, len(plain_text), self.block_size)]

        # Convert blocks into a Base 10 number
        numbers = [self.to_base_10(block, self.encrypt_alphabet) for block in blocks]

        # Read n and e from public.txt
        with open("public.txt", "r") as public_file:
            n = int(public_file.readline().strip())
            e = int(public_file.readline().strip())

        # Encrypt each base 10 num using RSA
        encrypted_blocks = [pow(number, e, n) for number in numbers]

        # Convert the resulting integers back to the base 70 alphabet
        encrypted_text = ''.join([self.base10_to_text(num, self.encrypt_alphabet) for num in encrypted_blocks])

        # Add block separators ($) after each block
        encrypted_text_with_blocks = '$'.join(encrypted_text[i:i + self.block_size] for i in
                                               range(0, len(encrypted_text), self.block_size))

        # Write resulting numbers to output file
        with open(output_file, "wb") as fout:
            fout.write(encrypted_text_with_blocks.encode("utf-8"))

    def decrypt(self, input_file, output_file):
        with open(input_file, "rb") as fin:
            encrypted_text_binary = fin.read()

        encrypted_text = encrypted_text_binary.decode("utf-8")

        encrypted_blocks = encrypted_text.split('$')

        with open("private.txt", "r") as private_file:
            n = int(private_file.readline().strip())
            d = int(private_file.readline().strip())

        numbers = [self.to_base_10(block, self.encrypt_alphabet) for block in encrypted_blocks]

        decrypted_blocks = [pow(number, d, n) for number in numbers]

        decrypted_text = ''.join([self.base10_to_text(num, self.encrypt_alphabet) for num in decrypted_blocks])

        with open(output_file, "wb") as fout:
            fout.write(decrypted_text.encode("utf-8"))

    def to_base_10(self, text, alphabet):
        base = len(alphabet)
        answer = 0
        for c in text:
            if c in alphabet:
                answer = answer * base + alphabet.index(c)
        return answer

    def base10_to_text(self, number, alphabet):
        base = len(alphabet)
        text = ''
        while number:
            number, remainder = divmod(number, base)
            text = alphabet[remainder] + text
        return text

    def inverse(self, a, n):
        t, newt = 0, 1
        r, newr = n, a

        while newr != 0:
            quotient = r // newr
            t, newt = newt, t - quotient * newt
            r, newr = newr, r - quotient * newr

        if r > 1:
            raise ValueError("a is not invertible")

        if t < 0:
            t += n
        return t
