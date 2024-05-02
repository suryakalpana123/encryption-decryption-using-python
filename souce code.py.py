from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
message =  input("Enter the message to be encrypted: ")
encrypted = encrypt_message(message)
print("Encrypted message:", encrypted)

decrypted = decrypt_message(encrypted)
print("Decrypted message:", decrypted)
