import hashlib
import time

print(".:WELCOME-TO-MD5/SHA512/SHA256/SHA224/SHA1-HASHER:.")
print(".::::::::::::::mAdE-bY-JuLiUS-AaLtO:::::::::::::::.")

while True:
    strHash = input("Anna sana jonka haluat salata: ")

    result_md5 = hashlib.md5(strHash.encode())
    result_sha512 = hashlib.sha512(strHash.encode())
    result_sha256 = hashlib.sha256(strHash.encode())
    result_sha224 = hashlib.sha224(strHash.encode())
    result_sha1 = hashlib.sha1(strHash.encode())
    
    print("TEXT:    " + strHash)
    print("SHA-512: " + result_sha512.hexdigest())
    print("SHA-256: " + result_sha256.hexdigest())
    print("SHA-224: " + result_sha224.hexdigest())
    print("SHA-1:   " + result_sha1.hexdigest())
    print("MD5:     " + result_md5.hexdigest())
    print("\n")

