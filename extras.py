import os
import shutil
import time
import sys
def Dchecker():
    if not os.path.exists("G:\\"):
        print("Drive not opened, trying to open it")
        time.sleep(1)
        try:
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Drive.lnk")
            print("opening")
        except:
            print("Drive wasn't found on the disk")
    else:
        print(".")