from Crypto.Protocol.KDF import PBKDF2

def derive_key(passphrase, salt, key_length=32, iterations=1000000):
    return PBKDF2(passphrase, salt, dkLen=key_length, count=iterations)
