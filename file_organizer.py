import os
import shutil

def organize_files():
folder = os.getcwd():
print(f"Organizing folder files in:{folder}")
for file in os.listdir(folder):
    if os.path.isfile(file):
        ext = file.split(".")[-1]
        ext_folder= os.path.join(folder, ext.upper())
        os.makedirs(ext_folder, exist_ok=True)
        shutil.move(file, os.path.join(ext_folder,file))
print("File organization complete\n")

