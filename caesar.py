def encrypt(key,plaintext):
    ciphertext=""
    for element in plaintext:
        code = ord(element) - 65
        new_code = code + key
        new_char = chr((new_code % 26) + 65)
        ciphertext += new_char
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    for element in ciphertext:
        code = ord(element) - 65
        new_code = code - key
        new_char = chr((new_code % 26) + 65)
        plaintext += new_char
    return plaintext
