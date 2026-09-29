import os
Idiomas=[]
for archive in os.listdir():
    if archive.endswith(".txt"):
        print(archive)
        Idiomas.append(archive)