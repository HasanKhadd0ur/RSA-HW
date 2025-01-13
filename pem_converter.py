import base64

class PEMConverter:
    @staticmethod
    def to_pem(key, key_type):
        """
        Convert a key to PEM format.
        - key: Tuple containing key components.
        - key_type: Either 'PUBLIC' or 'PRIVATE'.
        """
        key_bytes = f"{key[0]},{key[1]}".encode()
        key_base64 = base64.b64encode(key_bytes).decode()
        pem_key = f"-----BEGIN {key_type} KEY-----\n{key_base64}\n-----END {key_type} KEY-----"
        return pem_key

    @staticmethod
    def from_pem(pem_key):
        """
        Convert PEM-formatted key back to tuple.
        - pem_key: The PEM-formatted key string.
        """
        key_base64 = "".join(pem_key.split("\n")[1:-1])
        key_bytes = base64.b64decode(key_base64).decode()
        n, val = map(int, key_bytes.split(","))
        return n, val
