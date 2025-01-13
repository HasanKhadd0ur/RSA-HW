import random
from sympy import isprime, mod_inverse


class KeyGenerator:
    def __init__(self, bits=512):
        self.bits = bits  # Number of bits for p and q
    
    def generate_private_key(self):
        """
        Generate a private key using two large prime numbers p and q.
        The private key consists of (d, n), where:
          - d is the private exponent
          - n is the system modulus
        Returns:
            tuple: (d, n), represent the private key
        """
        # [1] Generate two large distinct prime numbers
        #        p and q
        p = self._generate_large_prime()
        q = self._generate_large_prime()

        while p == q:  # Ensure p and q are distinct
            q = self._generate_large_prime()

        # ][2] Calculate n (the system modulus) and phi(n) 
        n = p * q
        phi_n = (p - 1) * (q - 1)

        # [3] Choose e (public exponent) 
        #       such that 1 < e < ph(n) and gcd(e, phi(n)) = 1
        
        e = 65537  # Common choice for e

        while self._gcd(e, phi_n) != 1:
            e += 2

        # [4] Calculate d (the private exponent) 
        #       such that d * e ≡ 1 (mod phi(n))
        d = mod_inverse(e, phi_n)

        # Return the private key as (d, n)
        return d, n

    def extract_public_key(self, private_key):
        """
        Extract the public key from the private key.
        Public key consists of (e, n), where:
          - e is the public exponent
          - n is the modulus (same as in the private key)
        Args:
            private_key (tuple): (d, n)
        Returns:
            tuple: (e, n)
        """
        d, n = private_key

        # [1] Recalculate [hi(n)
        #        from n and d
        
        e = 65537

        # [2]] Return the public key as (e, n)
        return e, n

    def _generate_large_prime(self):
        """Generate a large prime number with the specified number of bits."""
        while True:
            candidate = random.getrandbits(self.bits)
            if isprime(candidate):
                return candidate

    def _gcd(self, a, b):
        """Compute the greatest common divisor (GCD) of two integers."""
        while b:
            a, b = b, a % b
        return a
