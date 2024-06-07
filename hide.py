from cryptography.fernet import Fernet

message = "hello"

key = Fernet.generate_key()

print(key)

fernet = Fernet(key)

enc_message = fernet.encrypt(message.encode())

print("original message: ", message)
print("encrypted message: ", enc_message)

dec_message = fernet.decrypt(enc_message).decode()

print(dec_message)


import rsa

public_key, private_key = rsa.newkeys(512)

message = "hello"

enc_message = rsa.encrypt(message.encode(), public_key)

print("original message: ", message)
print("encrypted string: ", enc_message)

dec_message = rsa.decrypt(enc_message, private_key).decode()

print("decrypted message: ", dec_message)

import sys
import hashlib

message = "hello"

if sys.version_info < (3,6):
    import sha3

encoded_str = message.encode()

print(encoded_str)

obj_sha3_512 = hashlib.sha3_512(encoded_str)

print(obj_sha3_512.hexdigest())












