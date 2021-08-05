import cv2
import os
import csv

def is_number(uid):
    try:
        float(uid)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(uid)
        return True
    except (TypeError, ValueError):
        pass

    return False

def take_image():

    uid = input("Enter your Uid: ")
    name = input("Enter your Name: ")

    if (is_number(uid) and name.isalpha()):
        
        cam = cv2.VideoCapture(0)
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        count = 0

        while True:

            ret,img = cam.read()

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray,1.5,5,minSize=(40,40),flags=cv2.CASCADE_SCALE_IMAGE)

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(58,50,168),2)

                count += 1

                cv2.imwrite("trainingdata"+os.sep+name+"."+uid+"."+str(count)+".jpg",gray[y:y+h,x:x+w])

                cv2.imshow("data",img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif count > 100:
                break
        cam.release()
        cv2.destroyAllWindows()

        res = "images are stored for id : "+str(uid)+" and Name : "+name

        row = [uid,name]

        with open("userdetails"+os.sep+"userdetails.csv",'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        
        csvFile.close()

    else:
        if is_number(uid):
            print("enter aphabetic name")
        if name.isalpha():
            print("enter numeric uid")
        if not is_number(uid) and not name.isalpha():
            print("enter numeric uid and aphabetic name")

take_image()
