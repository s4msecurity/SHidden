import os
import sys

print("""

..######..##.....##.####.########..########
.##....##.##.....##..##..##.....##.##......
.##.......##.....##..##..##.....##.##......
..######..#########..##..##.....##.######..
.......##.##.....##..##..##.....##.##......
.##....##.##.....##..##..##.....##.##......
..######..##.....##.####.########..########

S4m is a ready-to-use script for StegHide.

With this program you can use complex steghide commands without entering.
Be careful! StegHide software must be installed on your operating system. """)

def hide():
    print("====================================================================")
    print("Hide select")
    path = input("Show the path to the file you want to hide: ")
    photopath = input("Give the address of the image to hide: ")
    try:
        os.system("steghide embed -ef "+path+" -cf "+photopath)
    except:
        print("Error: Program path is incorrect or there is a problem with steghide.")
        hide()

def unveral():
    print("=====================================================================")
    print("Unveral select")
    encpath = input("Enter the path to remove the hidden file: ")
    try:
        os.system("steghide exract -sf "+encpath)
    except:
        print("Error: Program path is incorrect or there is a problem with steghide.")
        unveral()
def info():
    print("=====================================================================")
    print("Getting information for the file.")
    infopath = input("Show the path to the file to read: ")
    try:
        os.system("steghide info "+infopath)
    except:
        print("Error: Program path is incorrect or there is a problem with steghide.")

def start():
    print("""
    1. H/h => to hide file:
    2. U/u => to remove the hidden file:
    3. I/i => to collect data about the file: 
    """)

    select = input("Select => ")

    if select == "H" or select == "h" or select == "1":
        hide()
    elif select == "u" or select == "U" or select == "2":
        unveral()
    elif select == "I" or select == "i" or select == "3":
        info()
    else:
        print("Plase, input H, U or I!")
        start()
start()
