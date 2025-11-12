import hashlib
import base58
import binascii
from bitcoinutils.keys import PrivateKey
from bitcoinutils.setup import setup
import requests


# Library need install 
# bitcoin-utils~=0.7.3
# base58~=2.1.1
# pip install bitcoin-utils
# pip install base58
# https://bitcoin.therpc.io/
# https://api.blockeden.xyz/btc/67nCBdZQSH9z3YqDDjdm
# https://bitcoin.drpc.org/
# 
# RPC_URL = "https://bitcoin-rpc.publicnode.com"


## ====================================
my_string = input("Please enter string create BTC : ")
## ====================================

#  {"mainnet", "testnet", "testnet4", "signet", "regtest"}
setup("mainnet")

private_key_hex = hashlib.sha256(my_string.encode('utf-8')).hexdigest()

def private_key_to_wif(private_key_input, compressed=True):
    # 1. Add Prefix (and optional compression byte)
    extended_key = "80" + private_key_input
    if compressed:
        extended_key += "01"

    # 2. Double SHA-256 Hashing
    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

    # 3. Checksum
    checksum = second_sha256[:8]
    # 4. Append Checksum
    final_key_hex = extended_key + checksum

    # 5. Base58Check Encode
    wif_key = base58.b58encode(binascii.unhexlify(final_key_hex))
    return wif_key.decode('utf-8')  # Decode bytes to string for output

# Compressed WIF
wif_compressed = private_key_to_wif(private_key_hex, compressed=True)
print(f"Compressed WIF - Private Key: {wif_compressed}")

private_key = PrivateKey(wif=wif_compressed)
public_key = private_key.get_public_key()

# Generate the Base58, Bech32 P2WPKH address
base58_address = public_key.get_address(True)
bech32_address = public_key.get_segwit_address()

# =========================================================================
# Get Balance from Api mempool
mempool_api = "https://mempool.space/api/address/" #Change to local mempool instance
HTTPS_SCAN = "https://mempool.space/address/"

def get_balance(_address):
    url = f"{mempool_api}{_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
        last_balance = result.get("chain_stats", {}).get("funded_txo_sum", 0) - result.get("chain_stats", {}).get("spent_txo_sum", 0)
        tx_count = result.get("chain_stats", {}).get("tx_count", 0)
        return last_balance, tx_count
    except Exception as e:
        print(f"Error fetching balance for {_address}: {e}")
        return None, None

bal_base58, tx_base58 = get_balance(base58_address.to_string())
bal_bech32, tx_bech32 = get_balance(bech32_address.to_string())


print(f"Base58 Address: {HTTPS_SCAN}{base58_address.to_string()} = {bal_base58} | total tx = {tx_base58}")
print(f"Bech32 (P2WPKH) Address: {HTTPS_SCAN}{bech32_address.to_string()} = {bal_bech32} | total tx = {tx_bech32}")