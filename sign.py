from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

def sign(m):
	#generate public key
	#Your code here
	sk, pk = gen_keypair(secp256k1)
	public_key = pk

	#generate signature
	#Your code here
	sig = ecdsa.sign(m,sk,secp256k1,sha256,False)
	r = sig[0]
	s = sig[1]

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )


