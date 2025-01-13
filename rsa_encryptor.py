from sympy import mod_inverse

class RSAEncryptor:

    def encrypt(self,message, public_key):
        """
        Encrypts a message using the public key (e, n).
        """
        e, n = public_key

        # Convert plaintext to an integer
        message_int = int.from_bytes(message.encode(), 'big')

        # Perform encryption
        #      ciphertext = ( (message as int) ^ e) mod n
        ciphertext = pow(message_int, e, n)

        return ciphertext

    def decrypt(self,ciphertext, private_key):
        """
        Decrypts a ciphertext using the private key (d, n).
        """
        d, n = private_key
        # Perform decryption
        #    plaintext_int = (ciphertext ^ d) mod n
        plaintext_int = pow(ciphertext, d, n)
        # Convert integer back to bytes
        try:
            plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big')
            plaintext = plaintext_bytes.decode('utf-8', errors='replace')  # Replace invalid bytes
            return plaintext
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")
