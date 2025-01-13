from key_generator import KeyGenerator
from pem_converter import PEMConverter
from rsa_encryptor import RSAEncryptor

def main():
    print("\n\n\n\n")

    # [1] Key generation
    key_generator = KeyGenerator(bits=512)

    ## Generate a private key 
    private_key = key_generator.generate_private_key()
    ## Generate a public  key 
    public_key = key_generator.extract_public_key(private_key)
    
    print("Private Key:", private_key)
    print("Public Key:", public_key)

    # [2] Convert to PEM format

    pem_converter = PEMConverter() # defin pem formater 

    private_pem = pem_converter.to_pem(private_key, "PRIVATE") # format the priavte key
    public_pem = pem_converter.to_pem(public_key, "PUBLIC") # format the publiie key

    print("\nPrivate Key (PEM):\n", private_pem)
    print("\nPublic Key (PEM):\n", public_pem)

    # [3] Encrypt and decrypt a message

    ## Creata an Encrpytor
    rsa_encryptor= RSAEncryptor()
    
    message = "\n\nHello, RSA!"
    print("\nOriginal Message:", message)

    encrypted_message = rsa_encryptor.encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = rsa_encryptor.decrypt(encrypted_message, private_key)
    print("\n\nDecrypted Message:", decrypted_message)

    # [4] Convert PEM back to keys
    restored_private_key = pem_converter.from_pem(private_pem)
    restored_public_key = pem_converter.from_pem(public_pem)

    print("\nRestored Private Key:", restored_private_key)
    print("Restored Public Key:", restored_public_key)

if __name__ == "__main__":
    main()
