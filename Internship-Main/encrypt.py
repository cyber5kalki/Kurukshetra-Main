import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from utils import derive_key
import re

def validate_passphrase(passphrase):
    if len(passphrase) < 8:
        raise ValueError("Passphrase must be at least 8 characters long.")
    if not re.search(r'[a-z]', passphrase):
        raise ValueError("Passphrase must contain at least one lowercase letter.")
    if not re.search(r'[A-Z]', passphrase):
        raise ValueError("Passphrase must contain at least one uppercase letter.")
    if not re.search(r'[0-9]', passphrase):
        raise ValueError("Passphrase must contain at least one number.")
    if not re.search(r'[\W_]', passphrase):
        raise ValueError("Passphrase must contain at least one special character.")
    return passphrase

def encrypt_file(file_path, passphrase):
    try:
        # Validate passphrase
        validate_passphrase(passphrase)
        
        # Generate a random key for file encryption
        fek = get_random_bytes(32)  # File Encryption Key (FEK)
        iv = get_random_bytes(AES.block_size)
        salt = get_random_bytes(16)
        
        # Derive a key from the passphrase
        key = derive_key(passphrase, salt)
        
        # Encrypt the file
        cipher = AES.new(fek, AES.MODE_CBC, iv)
        with open(file_path, 'rb') as f:
            file_data = f.read()
        encrypted_file_data = iv + cipher.encrypt(pad(file_data, AES.block_size))
        
        # Overwrite the original file with the encrypted data
        with open(file_path, 'wb') as f:
            f.write(encrypted_file_data)
        
        # Encrypt the FEK with the derived key
        cipher_fek = AES.new(key, AES.MODE_CBC, iv)
        encrypted_fek = cipher_fek.encrypt(pad(fek, AES.block_size))
        
        # Save the encrypted FEK with salt
        fek_file_path = file_path + '.fek'
        with open(fek_file_path, 'wb') as f:
            f.write(salt + iv + encrypted_fek)
        
        return f"File '{file_path}' has been encrypted.\nEncrypted FEK saved to '{fek_file_path}'"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import sys
    import getpass
    if len(sys.argv) != 2:
        print("Usage: python encrypt.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    passphrase = getpass.getpass("Enter passphrase: ")
    result = encrypt_file(file_path, passphrase)
    print(result)
