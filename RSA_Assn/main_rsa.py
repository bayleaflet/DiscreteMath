# BJC, Original Author
# 4/1/2024

# Main function that instantiates RSA class, generates keys, encrypts, and
# decrypts.
from cp_RSA import RSA

def main():
    # Initialize RSA object
    rsa = RSA()

    # Generate RSA keys
    p, q = rsa.generate_keys()

    # Encrypt a file
    input_file = "plain_text.txt"
    output_file_encrypted = "encrypted_output.txt"
    rsa.encrypt(input_file, output_file_encrypted)
    print("File encrypted successfully.")

    # Decrypt the encrypted file
    input_file_encrypted = output_file_encrypted
    output_file_decrypted = "decrypted_output.txt"
    rsa.decrypt(input_file_encrypted, output_file_decrypted)
    print("File decrypted successfully.")

if __name__ == "__main__":
    main()
