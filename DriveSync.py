import os
import shutil
import sys
import time
import extras
import MainCode
while True:
    extras.Dchecker()
    q = input("Welcome, what do you want, to copy to drive (1) or to copy from drive (2)")
    if q == "1":
        start, finish = MainCode.folderselection()
        MainCode.copy(start, finish)
        break
    elif q == "2":
        start2, finish2 =  MainCode.folderselection()
        MainCode.copy2(start2, finish2)
        break
    else:
        print("invalid")
        break
            




