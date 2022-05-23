import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    #Collision finding code goes here
    x = os.urandom(6)
    x_hash_bytes = hashlib.sha256(x).hexdigest()
    x_value = int.from_bytes(bytes.fromhex(x_hash_bytes), byteorder='big', signed=False)
    y = b'\x00'
    y_value = 0
    print(x_hash_bytes, hashlib.sha256(y).hexdigest())
    while not last_k_bits_match(x_value,
                                int.from_bytes(bytes.fromhex(hashlib.sha256(y).hexdigest()),
                                               byteorder='big',
                                               signed=False),
                                k):
        y_value += 1;
        y = str(y_value).encode()

    return( x, y )

def last_k_bits_match(x_value, y_value, k):
    if k == 0:
        return True
    mask = 0
    for i in range(k):
        mask = mask << 1
        mask |= 1
    masked_x = x_value & mask
    masked_y = y_value & mask

    return masked_x == masked_y