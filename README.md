# RSA Encryption and Decryption

This project implements the RSA algorithm for encrypting and decrypting messages. And It includes generating private keys, extracting public keys, and performing encryption and decryption operations. The implementation is designed with modularity and reusability in mind.


[souce codee](https://git.hiast.edu.sy/hasan.bahjat/rsa_hw)

____

## Features
- **Key Generation**:
  - Generate private keys using large prime numbers.
  - Extract public keys from private keys.
- **Encryption and Decryption**:
  - Encrypt plaintext messages using the public key.
  - Decrypt ciphertext messages using the private key.

## Project Structure
```
.
├── key_generator.py  # Generates private and public keys
├── rsa_encryptor.py  # Handles encryption and decryption
├── main.py           # Demonstrates usage of the RSA implementation
├── Makefile          # Automates setup, testing, and execution
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```


## Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Run the Demo
1. Execute the main script to generate keys, encrypt a message, and decrypt it:
   ```bash
   python main.py
   ```

2. Example Output:
   ```
   Private Key: (d, n)
   Public Key: (e, n)

   Original Message: Hello, RSA!
   Encrypted Message: <ciphertext>
   Decrypted Message: Hello, RSA!
   ```

### Automate with Makefile
- **Run the project**:
  ```bash
  make run
  ```
- **Clean up bytecode files**:
  ```bash
  make clean
  ```

## Key Format
- **Private Key**: `(d, n)`
  - `d`: Private exponent
  - `n`: Modulus
- **Public Key**: `(e, n)`
  - `e`: Public exponent (default: `65537`)
  - `n`: Modulus

# Some Imgs 

![alt text](<assets/Screenshot 2025-01-13 194958.png>)

![alt text](<assets/Screenshot 2025-01-13 195104.png>)

![alt text](<assets/Screenshot 2025-01-13 195134.png>) 