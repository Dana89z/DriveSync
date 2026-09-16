import os
import shutil
import time
import sys
timee = time.strftime("%d-%m-%Y-%H-%M-%S")
print(f"creating backup, {timee}")
user = os.path.expanduser("~")
def checkfordrive():
    if os.path.exists("G:\\"):
        print("Google drive found")
        return True
    else:
        print("Not found, open desktop Drive")
        return False


check = checkfordrive()

if check == True:
    name = f"Python_{timee}"
    
    origen = os.path.join(user, "Desktop", "Antigravity")
    destino = os.path.join("G:\\", "Mi Unidad", "Python", name)



    os.makedirs(destino, exist_ok=True)
    for archivo in os.listdir(origen):
        ruta_origen = os.path.join(origen, archivo)
        ruta_destino = os.path.join(destino, archivo)
        
        if os.path.isfile(ruta_origen):
            shutil.copy2(ruta_origen, ruta_destino)
            print(f"Copied {archivo}")
        elif os.path.isdir(ruta_origen):
            shutil.copytree(ruta_origen, ruta_destino, dirs_exist_ok=True)
            for subfile in os.listdir(ruta_origen):
                print(f"Copied {subfile} from {archivo}")
    input("Press any key to close: ")
else:
    print("Drive was not found, opening it")
    time.sleep(1)
    drive = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Drive.lnk"
    if os.path.exists(drive):
        os.startfile(drive)
        print("Opening Succesful")
        time.sleep(1)
        print("giving it 3 seconds")
        for number in range(0, 3):
            print(number)
            time.sleep(1)
        print("Trying to open back script")
        try:
            os.startfile(os.path.join(user, "Desktop", "Antigravity", "RealProyects", "DriveSync.py"))
        except Exception as e:
            print(e)
            print("Not working ig")
            print("open it manually mf")
          

        

    else:
        print("Not found")


            




