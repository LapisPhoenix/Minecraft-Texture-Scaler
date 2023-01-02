# Made by Lapis Pheonix
# If you show it off, please credit

from os import listdir
from PIL import Image
from time import time


images = 0
ignored = 0
DIRECTORY_URL = input("Texture Folder Directory: ").replace('\\', '\\\\') 
if DIRECTORY_URL.endswith("\\" or "\\\\"):
     pass
else:
     DIRECTORY_URL += '\\'

print("Finding Textures...", end='\r')
try:
    listdir(DIRECTORY_URL)
    if len(listdir(DIRECTORY_URL)) == 0:
         exit("Found directory but it was empty!")
except FileNotFoundError:
     exit("Directory not found!")
else:
     print("Found directory!")

done = False
while not done:
    try:
        size = int(input("Original Resolution: "))
    except ValueError:
        print("Original resolution must be an number! EX: 16")
    
    try:
        new_size = int(input("New Resolution: "))
        done = True
    except ValueError:
         print("New resolution must be an number! EX: 256")

print("Editing Textures...", end='\r')

start = time()
try:
    for file in listdir(path=DIRECTORY_URL):
        if file.endswith(".png"):
            image = Image.open(DIRECTORY_URL + f"{file}")
            if image.size == (size, size):
                    new = image.resize(size=(new_size, new_size), resample=Image.Resampling.NEAREST)
                    new.save(DIRECTORY_URL + file)
                    images += 1
            elif image.size != (size, size):
                ignored += 1
except Exception as e:
     print("Couldn't procces {0} with error:\n{1}".format(file, e.__str__))

print("Done editing textures!", end='\r')
print(f"Took {round(time() - start, 2)} seconds to edit {images} textures. (Ignored {ignored} files.)")