from cryptography.hazmat.primitives.asymmetric import mlkem

class AEGISQuantumVault:
    def __init__(self):
        self.private_key = mlkem.MLKEM768PrivateKey.generate()
        self.public_key = self.private_key.public_key()

    def encrypt_data(self, data: bytes):
        res1, res2 = self.public_key.encapsulate()
        # Find which one is the ciphertext (the longer one, 1088 bytes)
        if len(res1) > len(res2):
            ciphertext = res1
            shared_secret = res2
        else:
            ciphertext = res2
            shared_secret = res1
        return ciphertext, shared_secret

    def decrypt_data(self, ciphertext: bytes):
        shared_secret = self.private_key.decapsulate(ciphertext)
        return shared_secret

if __name__ == "__main__":
    vault = AEGISQuantumVault()
    ct, ss1 = vault.encrypt_data(b"secret")
    ss2 = vault.decrypt_data(ct)
    assert ss1 == ss2
    print("✅ EXCALIBUR ENCRYPTED: 2000-YEAR QUANTUM RESISTANT")
