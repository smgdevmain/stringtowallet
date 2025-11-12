import hashlib
import binascii
from solders.keypair import Keypair
from solana.rpc.api import Client
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

# Library need install 
# pip install solana
# pip install solders
# pip install cryptography
# https://solana.drpc.org/
# https://solana-rpc.publicnode.com
# https://solana.lavenderfive.com/

# Base58 alphabet (same as Bitcoin/Solana)
B58_DIGITS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

HTTPS_SCAN = "https://solscan.io/account/"
RPC_URL = "https://solana-rpc.publicnode.com"

solana_client = Client(RPC_URL) # connect RPC for get Balance SOL

## ====================================
my_string = input("Please enter string to Create Sol : ")
## ====================================


def base58_encode(data: bytes) -> str:
    """Pure Python Base58 encode function."""
    # Convert bytes to integer
    n = int('0x0' + binascii.hexlify(data).decode('utf8'), 16)
    
    # Divide into base58
    res = []
    while n > 0:
        n, r = divmod(n, 58)
        res.append(B58_DIGITS[r])
    res = ''.join(res[::-1])
    
    # Encode leading zeros
    pad = 0
    for c in data:
        if c == 0:
            pad += 1
        else:
            break
    return B58_DIGITS[0] * pad + res


def sha256_hash_to_base58(sha256_hash: bytes) -> str:
    """
    Convert a 32-byte SHA-256 hash (as seed) to a Base58-encoded Solana private key.
    
    :param sha256_hash: 32-byte SHA-256 hash as bytes (the seed).
    :return: Base58-encoded Solana private key (64 bytes encoded).
    """
    if len(sha256_hash) != 32:
        raise ValueError("Input must be exactly 32 bytes (SHA-256 hash).")
    
    # Derive the clamped scalar from SHA-512 of the seed
    h = hashlib.sha512(sha256_hash).digest()
    a = bytearray(h[:32])
    a[0] &= 248  # Clear the lowest 3 bits
    a[31] &= 127  # Clear the highest bit
    a[31] |= 64   # Set the second highest bit
    scalar = bytes(a)
    
    # Generate the Ed25519 private key and public key bytes
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(scalar)
    public_key = private_key.public_key()
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    
    # Solana private key is scalar (32 bytes) + public key (32 bytes)
    solana_secret = scalar + public_bytes
    
    # Base58 encode
    return base58_encode(solana_secret)

# 1. Create a SHA-256 hash object
sha256_hash_bytes = hashlib.sha256(my_string.encode('utf-8')).digest()

# 2 . Base58 Private Key Solana
base58_private_key = sha256_hash_to_base58(sha256_hash_bytes)

# 3. Generate Pubkey
public_key = Keypair.from_base58_string(base58_private_key).pubkey()

# ===================================================================================
print(f"Private Key : {base58_private_key} \n\t => {HTTPS_SCAN}{str(public_key)}")
print(f"Check Balance ...")

balance  = solana_client.get_balance(public_key).value
print(f"Balance : {balance/10**9} SOL")