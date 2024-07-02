import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from utils import derive_key

def decrypt_file(encrypted_file_path, fek_file_path, passphrase):
    try:
        if not os.path.exists(encrypted_file_path):
            return f"Error: Encrypted file '{encrypted_file_path}' not found."
        if not os.path.exists(fek_file_path):
            return f"Error: FEK file '{fek_file_path}' not found."
        
        # Read and decrypt the FEK
        with open(fek_file_path, 'rb') as f:
            salt = f.read(16)
            iv = f.read(AES.block_size)
            encrypted_fek = f.read()
        
        key = derive_key(passphrase, salt)
        cipher_fek = AES.new(key, AES.MODE_CBC, iv)
        fek = unpad(cipher_fek.decrypt(encrypted_fek), AES.block_size)
        
        # Read and decrypt the file
        with open(encrypted_file_path, 'rb') as f:
            iv = f.read(AES.block_size)
            encrypted_file_data = f.read()
        
        cipher = AES.new(fek, AES.MODE_CBC, iv)
        file_data = unpad(cipher.decrypt(encrypted_file_data), AES.block_size)
        
        # Save the decrypted file
        decrypted_file_path = encrypted_file_path.rstrip('.enc')
        with open(decrypted_file_path, 'wb') as f:
            f.write(file_data)
        
        # Remove the FEK file only after successful decryption
        os.remove(fek_file_path)
        
        return f"File '{os.path.basename(decrypted_file_path)}' decrypted successfully and '{os.path.basename(fek_file_path)}' FEK file removed."
    except ValueError:
        return "Incorrect password"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import sys
    import getpass
    if len(sys.argv) != 3:
        print("Usage: python decrypt.py <encrypted_file_path> <fek_file_path>")
        sys.exit(1)
    
    encrypted_file_path = sys.argv[1]
    fek_file_path = sys.argv[2]
    passphrase = getpass.getpass("Enter passphrase: ")
    result = decrypt_file(encrypted_file_path, fek_file_path, passphrase)
    print(result)
    sys.exit()
