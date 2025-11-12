import hashlib
import web3
from web3 import Account

# Library need install 
# pip install web3

HTTPS_SCAN = "https://etherscan.io/address/"
RPC_URL = "https://ethereum.publicnode.com"
w3 = web3.Web3(web3.HTTPProvider(RPC_URL))

## ====================================
my_string = input("Please enter string to Create ETH : ")
## ====================================

# Create a SHA-256 hash object
sha256_hash = hashlib.sha256(my_string.encode('utf-8') )
# Get the hexadecimal representation of the hash
private_key = sha256_hash.hexdigest()

print(f"String: {my_string} => {private_key}")

# ==========================================================
address_result =  Account.from_key(private_key).address
balance = w3.eth.get_balance(address_result)

print(f"PrivateKey: {private_key} ==> Address : {HTTPS_SCAN}{address_result} | Balance : {balance} ")
