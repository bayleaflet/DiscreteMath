import miller_alg
import math

class RSA:

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.encrypt_alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


    def generate_keys(self):
        while True:
            string1 = input("Please enter first string: ")
            string2 = input("Please enter second string: ")
            # Convert p and q to base 10 using alphabet above
            p = self.to_base_10(string1, self.alphabet)
            q = self.to_base_10(string2, self.alphabet)

            # p and q need to be 200 or more digits long
            if p >= 2 and q >= 2:
                break
            else:
                print("Your input strings are too short. Try again.")
                continue

        # Mod p and q so they aren't too long
        p = p % 10 ** 200
        q = q % 10 ** 200

        # Make sure p and q are odd
        if p % 2 == 0:
            p += 1
        if q % 2 == 0:
            q += 1

        # Pass in p and q into Miller's algorithm
        # If Miller's returns True, answer is a probable prime
        while True:
            # Run Miller's Algorithm. If returns False...
            if not miller_alg.main(p):
                # Number is definitely composite. Continue loop.
                # We add 2 to keep number odd
                p += 2
                continue
            if not miller_alg.main(q):
                q += 2
                continue
            break

        # Assign n, r, e, and d
        n = p * q
        r = (p - 1) * (q - 1)

        # Find e -> a 398 digit number relatively prime with r
        # Making this smaller for testing purpose
        # e = 10 ** 398 + 1
        e = 65537
        while math.gcd(e,r) != 1:
            e += 1

        # Find d -> the inverse of e mod r
        d = self.inverse(e, r)

        print (" P is: ", str(p))
        print (" Q is: ", str(q))
        print (" E is: ", str(e))
        print (" R is: ", str(r))
        print (" D is: ", str(d))
        print (" N is: ", str(n))
        print (" At this time, these numbers are being written to public + private correctly")
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
        # Read n and e from public.txt
        with open("public.txt", "r") as public_file:
            n = int(public_file.readline().strip())
            e = int(public_file.readline().strip())

        # Open input file in binary mode, read contents
        with open(input_file, "rb") as fin:
            plain_text_binary = fin.read()

        # Decode binary data into a Unicode str using UTF-8 encoding
        plain_text = plain_text_binary.decode("utf-8")

        #WORKING TO THIS POINT
        max_bytes_per_block = (math.log(n,70))
        print("Max byte per block: ", max_bytes_per_block)
        plain_text_length = len(plain_text)
        blocks_reqd = math.ceil(plain_text_length/max_bytes_per_block)
        print("blocks required: ", blocks_reqd)
        bytes_per_block = plain_text_length//blocks_reqd
        print("bytes per block: ", bytes_per_block)
        print('')

        # Loops thru blocks, encode
        encode_blocks=[]
        for i in range(blocks_reqd):
            if i == (blocks_reqd-1):
                plain_text_block = plain_text[i*bytes_per_block:]
            else:
                plain_text_block = plain_text[i*bytes_per_block:(i+1)*bytes_per_block]

            plain_block = self.to_base_10(plain_text_block, self.encrypt_alphabet)
            encrypt_block = pow(plain_block, e, n)
            encrypt_text_block = self.base10_to_text(encrypt_block, self.encrypt_alphabet)
            encrypt_text_block += "$"
            encode_blocks.append(encrypt_text_block)

        print("Plain block: ", plain_block)

        print ("Encrypted blocks: ", encrypt_block)

        print("Encrypted_text: ", encrypt_text_block)

        print("Encrypted text with blocks: ", encode_blocks)

        # Write resulting numbers to output file
        fout = open(output_file, 'wb')
        for block in encode_blocks:
            fout.write(block.encode('utf-8'))
        fout.close()

    def decrypt(self, input_file, output_file):
        # Open input file in binary mode and read contents
        with open(input_file, "rb") as fin:
            encrypted_text_binary = fin.read()
        # Decode binary data into Unicode str using UTF-8 encoding
        encrypted_text = encrypted_text_binary.decode("utf-8")

        # Split encrypted text into blocks separated by $ sign
        encrypted_blocks = encrypted_text.split('$')

        # Read n, d from private.txt
        with open("private.txt", "r") as private_file:
            n = int(private_file.readline().strip())
            d = int(private_file.readline().strip())

        # Convert each block into base 10 num
        numbers = [self.to_base_10(block, self.encrypt_alphabet) for block in encrypted_blocks]

        # Decrypt each base 10 num using RSA
        decrypted_blocks = [pow(number, d, n) for number in numbers]

        # Convert the resulting integers back
        decrypted_text = ''.join([self.base10_to_text(num, self.encrypt_alphabet) for num in decrypted_blocks])

        # Write decrypted text to output file in binary
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

