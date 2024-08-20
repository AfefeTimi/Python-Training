from datetime import datetime
from cryptography.fernet import Fernet

name = input("What is your name? ")
print("Welcome " + name)
current_time = datetime.now()
print("The time is ", current_time)
docu = open("logindocument.txt", "a")

docu.write(name + " " + str(current_time) + "\n")
docu.close()


# Generate a key (this should ideally be generated once and securely stored)
key = Fernet.generate_key()

# Create a Fernet object with the key
cipher_suite = Fernet(key)

# Encrypt a message
message = b"Hello, world!"
cipher_text = cipher_suite.encrypt(message)

print("Cipher Text:", cipher_text)

# Decrypt the message (to verify encryption)
plain_text = cipher_suite.decrypt(cipher_text)
print("Decrypted Text:", plain_text.decode())