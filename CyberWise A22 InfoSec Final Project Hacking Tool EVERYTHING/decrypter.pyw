# The purpose of this program is to decrypt the files and photos that were encryoted using my "final_tool.py" program.
# NOTE: Make sure the "crypt.key" file remains the same used to encrypt the files!!!


# The cryptography module must be installed with pip.
from cryptography.fernet import Fernet
import os


# The variable "directory" defines where all our encrypted files were put. This is the same as the "directory" variable defined in "final_tool.py".
# We will read files that are in subfolders, as well.

directory = os.getcwd()+"\log_files"


keyFile=open("crypt.key", "rb")
encryption_key=keyFile.read()
keyFile.close()
fernet_key = Fernet(encryption_key)


# We use the "os.walk()" function to go through our "directory" we call "focus" and grab all the files we called "files".
# It grabs files in subdirectories as well, so our screenshots are included!
# All files are added to the "files_to_decrypt" list.
# We use error handling just in case one of the files isn't encrypted, we can continue with the others.
# 1) We "read" "each_file" in our "files_to_decrypt" list in "binary",
# 2) We decrypt the encryption data using the key.
# 3) We overwrite each file's encrypted data with the non-encrypted binary data.

def decrypt_all_files():
    files_to_decrypt = []
    for focus, Folders, files in os.walk(directory):
        for file in files:
            each_file = os.path.join(focus,file)
            files_to_decrypt.append(each_file)
            
    for each_file in files_to_decrypt:
        try:
            with open(each_file, "rb") as f:
                encryption = f.read()
            decrypted = fernet_key.decrypt(encryption)
            with open(each_file, "wb") as f:
                f.write(decrypted)
        except:
            pass

decrypt_all_files()
