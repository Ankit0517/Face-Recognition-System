import os
import cv2
import pandas as pd
import time
import datetime

def recog_attendance():
    recog = cv2.face_LBPHFaceRecognizer.create()

    recog.read("traindata"+os.sep+"train.yml")

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    df = pd.read_csv("userdetails"+os.sep+"userdetails.csv")

    font = cv2.FONT_HERSHEY_SIMPLEX

    attnd_col_names = ["uid","name","date","time"]

    attendance = pd.DataFrame(columns=attnd_col_names)

    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    cam.set(3,1024)
    cam.get(4,768)

    minw = 0.1 * cam.get(3)

    minh = 0.1 * cam.get(4)

    while True:
        ret,img = cam.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.5,5,minSize=(40,40),flags=cv2.
        CASCADE_SCALE_IMAGE)

        for(s,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(58,50,168),2)

            uid, conf = recog.predict(gray[y:y+h,x:x+w])
            cv2.imshow("data",img)

            if conf < 100:
                data = df.loc[df['uid'] == uid]['name'].values

                confstr = " {0}".format(round(100-conf))

                data_t = str(uid)+"-"+data

            else:
                uid = "unknown"
                data_t = str(uid)

                confstr = " {0}".format(round(100-conf))

            if (100-conf) > 60:
                s_time = time.time()
                s_date = datetime.datetime.fromtimestamp(s_time).strftime("%Y-%m-%d")
                timestamp = datetime.datetime.fromtimestamp(s_time).strftime("%H:%M:%S")

                name = str(data)[2:-2]
                attendance.loc[len(attendance)] = [uid,name,s_date,timestamp]

            if (100-conf) > 60:
                 name  =name + " [pass]"
                 cv2.putText(img,str(name),(x+4,y+4),font,1,(58,50,168),2)

            elif(100-conf) > 50:
                name = name+ " [consider]"
                cv2.putText(img,str(name),(x+4,y+4),font,1,(255,255,255),2)     
                
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
recog_attendance()        

