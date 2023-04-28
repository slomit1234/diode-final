import os

filename = "test.txt"
filesize = 20 * 1024 * 1024 # 10 MB

with open(filename, "wb") as f:
    f.write(os.urandom(filesize))