import os
import Check_Camera #import file as module
import capture_faces #import file as module

def header():
    os.system('cls')
    print("--------------------------")
    print("-----Face Recognition-----")
    print("--------------------------")

def mainmenu():
    header()
    print("\n\n")
    print("----------options-----------")
    print("Choose 1 for checking camera.")
    print("Choose 2 for capturing faces.")

    while True:
        try:
            option_choice = input("Enter operation choice: ")
            if option_choice=="1":
                checkCam()
                #use checkcam as me method
                #os.system("python checkcamera.py") #can also call checkcamera file directly like this
            elif option_choice=="2":
                captureFaces()
        except:
            print("Invalid operation.")
    exit

def checkCam():
    check_camera.check_camera_def()
    key = input("return to main menu")
    mainmenu()

def captureFaces():
    capture_faces.take_image()
    key1 = input("Return to main menu")
    mainmenu()


mainmenu()