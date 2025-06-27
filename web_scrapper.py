import os
def clean_temp(files):
    folder = os.getcwd()
    print("Cleaning .tmp files...")
    for file in os.listdir(folder):
        if file.endswith(".tmp"):
            os.remove(file)
            print("Temp files cleaned.\n")

