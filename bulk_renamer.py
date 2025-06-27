import os
def bulk_rename():
    folder =os.getcwd()
    prefix ="AutoTasker_"
    count= 1

    print("Renameing files...")
    for file in os.listdir(folder):
        if os.path.isfile(file):
            ext =file.split(".")[-1]
            new_name= f"{prefix}{count}.{ext}"
            os.rename(file,new_name)
            count += 1
            print("Bulk rename complet.\n")