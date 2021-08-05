def check_camera_def():
    import cv2

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0) 

    while True:
        _,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.5,5,minSize=(40,40),flags=cv2.CASCADE_SCALE_IMAGE)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(58,50,168),2)

        cv2.imshow("testing cam",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            cv2.destroyAllWindows()
            break
check_camera_def()

