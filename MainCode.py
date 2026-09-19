import os
import shutil
import time
import sys


timee = time.strftime("%d-%m-%Y-%H-%M-%S")
print(f"creating backup, {timee}")
user = os.path.expanduser("~")
def checkfordrive():
    if os.path.exists("G:\\"):
        return True
    else:
        return False

drivecheck = checkfordrive()
drive = os.path.join("G:\\")


def folderselection():
    foldertocopy = input("Copy the route to the folder to copy")
    if os.path.exists(foldertocopy):
        print(f"{foldertocopy}, exists")
    else:
        print(f"{foldertocopy}, not found")

    foldertopaste = input("Copy the route of where you want it to be pasted")
    if os.path.exists(foldertopaste):
        print(f"{foldertopaste} exists")
    else:
        print(f"{foldertopaste}, doesn't exist")
    
    return foldertocopy, foldertopaste


def copy(foldertocopy, foldertopaste):
    if checkfordrive():
        if os.path.exists(foldertocopy):
            if os.path.exists(foldertopaste):
                finaldestination = os.path.join(foldertopaste, timee)
                os.makedirs(finaldestination, exist_ok=True)
                for item in os.listdir(foldertocopy):
                    ruta_origen = os.path.join(foldertocopy, item)
                    if os.path.isfile(ruta_origen):
                        shutil.copy2(ruta_origen, finaldestination)
                    else:
                        if os.path.isdir(ruta_origen):
                            ruta_sub_destino = os.path.join(finaldestination, item)
                            shutil.copytree(ruta_origen, ruta_sub_destino, dirs_exist_ok=True)
        else:
            print(f"{foldertocopy} doesn't exist")
          



def copy2(foldertocopy, foldertopaste):
    if checkfordrive():
        if os.path.exists(foldertocopy):
            if os.path.exists(foldertopaste):
                finaldestination = os.path.join(foldertopaste, "Backup")
                os.makedirs(finaldestination, exist_ok=True)
                for item in os.listdir(foldertocopy):
                    ruta_origen = os.path.join(foldertocopy, item)
                    if os.path.isfile(ruta_origen):
                        shutil.copy2(ruta_origen, finaldestination)
                    else:
                        if os.path.isdir(ruta_origen):
                            ruta_sub_destino = os.path.join(finaldestination, item)
                            shutil.copytree(ruta_origen, ruta_sub_destino, dirs_exist_ok=True)
        else:
            print(f"{foldertocopy} doesn't exist")






if __name__ == "__main__":
    foldertocopy, foldertopaste = folderselection()
    copy()