import unittest
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# Assuming the original functions are in a file named 'crypto_module.py'
from Encryptoin_Decryption  import vencrypt, vdecrypt, encrypt, decrypt

class TestEncryptionFunctions(unittest.TestCase):

    def setUp(self):
        # This will run before each test
        self.key = "testkey"
        self.msg = "HelloWorld"
        self.hkey = SHA256.new(self.key.encode('utf-8')).digest()

    def test_vencrypt(self):
        encrypted_msg = vencrypt(self.msg, self.key)
        # Ensure the encrypted message is not the same as the original
        self.assertNotEqual(encrypted_msg, self.msg)

    def test_vdecrypt(self):
        encrypted_msg = vencrypt(self.msg, self.key)
        decrypted_msg = vdecrypt(encrypted_msg, self.key)
        # Ensure the decrypted message is the same as the original
        self.assertEqual(decrypted_msg, self.msg)

    def test_encrypt(self):
        encrypted_msg = encrypt(self.hkey, self.msg.encode('utf-8'))
        # Ensure the encrypted message is not the same as the original
        self.assertNotEqual(encrypted_msg, self.msg.encode('utf-8'))

    def test_decrypt(self):
        encrypted_msg = encrypt(self.hkey, self.msg.encode('utf-8'))
        decrypted_msg = decrypt(self.hkey, encrypted_msg)
        # Ensure the decrypted message is the same as the original
        self.assertEqual(decrypted_msg, self.msg.encode('utf-8'))

if __name__ == '__main__':
    unittest.main()
