# Firstly run the following command in order to install the cryptodome module 
# (https://pycryptodome-master.readthedocs.io/en/latest/index.html)
# pip install pycryptodome

from Crypto.Cipher import AES
from base64 import b64encode

key = "Sixteen_byte_key".encode("utf-8")
plain = "Secret: 16 bytes".encode("utf-8")
iv = "Initialization v".encode("utf-8")

def encECB(key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertextECB = cipher.encrypt(plain)
    ct = b64encode(ciphertextECB).decode('utf-8')
    print (ct)


def encCBC(key):
    cipher = AES.new(key,AES.MODE_CBC, iv)
    ciphertextCBC = cipher.encrypt(plain)
    ct = b64encode(ciphertextCBC).decode("utf-8")
    print(ct)

if __name__ == "__main__":
    encECB(key)
    encCBC(key)
    