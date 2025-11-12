# StringToWallet Project
Create A wallet ETH, SOL, BTC from String input .

# Crypto Wallet Generator from Input String

A lightweight Python project to generate cryptocurrency wallets for **Solana (SOL)**, **Ethereum (ETH)**, and **Bitcoin (BTC)** from a user-provided input string.

This project includes **3 main files**:
- `string_wallet_eth.py` – Generate Ethereum wallet (address + private key)
- `string_wallet_sol.py` – Generate Solana wallet (address + private key)
- `string_wallet_btc.py` – Generate Bitcoin wallet (address + WIF private key)

## Features
- Deterministic wallet generation from a **custom string**
- Supports **Solana**, **Ethereum**, and **Bitcoin**
- Uses standard cryptographic libraries (`web3`, `solana`, `solders`, `bitcoin-utils`, `base58`, `cryptography` )

## Requirements
- Python 3.8+
- `pip` (Python package manager)

---

## Prerequisites

### 1. Install Python 3.13+

#### Windows
1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download **Python 3.13 or higher**
3. Run the installer
4. **Check "Add Python to PATH"** during installation

#### macOS
```bash
# Using Homebrew (recommended)
brew install python@3.13

# Or download from python.org
```

#### Linux (Ubuntu/Debian)
```
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

Verify installation:
python3 --version
on Windows:
python --version
```

Verify pip is Installed
```
pip --version
# or
python3 -m pip --version
```

#### Project Setup

```
1. Clone the Repositorybash or Download Zip to save and UnZip in a Folder for Project

git clone https://github.com/smgdevmain/stringtowallet.git
cd stringtowallet

2. Create a Virtual Environment On window / Linux: (create subfolder 'env' in your project)
python3 -m venv env

Windows:cmd
python -m venv env

3. Activate the Virtual EnvironmentmacOS / Linux: (need activate pip, python first to run)
source env/bin/activate

Windows:cmd
source env/bin/activate

You should now see (env) at the start of your terminal prompt.

4. Install Dependenciesbash (Install All Library for project)

pip install --upgrade pip
pip install -r requirements.txt
```

requirements.txt includes: (If you only run eth, install only 'web3' pip install web3)
```
web3~=7.8.0
bitcoin-utils~=0.7.3
base58~=2.1.1
solana~=0.36.9
solders~=0.27.0
cryptography~46.0.3
```

#### How to Run

```
# Ethereum
python string_wallet_eth.py

# Solana
python string_wallet_sol.py

# Bitcoin
python string_wallet_btc.py
```
