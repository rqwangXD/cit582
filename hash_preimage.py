import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    k = len(target_string)
    x_value = int(target_string, 2)
    nonce = os.urandom(4)
    # print('first nonce: ', nonce)
    while True:
        nonce_hash_value = int.from_bytes(bytes.fromhex(hashlib.sha256(nonce).hexdigest()),
                                          byteorder='big',
                                          signed=False)
        #print(hashlib.sha256(nonce).hexdigest())
        if last_k_bits_match(x_value, nonce_hash_value, k):
            break;
        else:
            nonce_value = int.from_bytes(nonce, byteorder='big', signed=False)
            # print('nonce_value: ', nonce_value)
            nonce_value += 1
            nonce = nonce_value.to_bytes((nonce_value.bit_length() + 7) // 8, byteorder='big')
            # print('next nonce: ', nonce)

    # print('final hash: ', hashlib.sha256(nonce).hexdigest())
    return( nonce )

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