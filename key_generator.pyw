# The purpose of this script is to generate a random binary key you can use to encrypt and decrypt files.
# CAUTION: DO NOT RUN THIS SCRIPT IF YOU HAVE FILES THAT ARE CURRENTLY ENCRYPTED!!! 
# CAUTION: RUNNING THIS SCRIPT WILL GENERATE A NEW KEY AND REPLACE THE OLD KEY, LEAVING YOU WITHOUT THE NECESSARY KEY TO DECRYPT YOUR FILES THAT WERE ENCRYTED WITH THE OLD KEY!!!


# The cryptography module must be installed with pip.
from cryptography.fernet import Fernet


# We generate a random binary-string key with cryptography's function, Fernet.

key = Fernet.generate_key()


# We write that key into a ".key" file.

crypt_doc=open("crypt.key", "wb")
crypt_doc.write(key)
crypt_doc.close()
