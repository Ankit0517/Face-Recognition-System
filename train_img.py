import os
from PIL import Image
import numpy as np
import time
import cv2
from threading import Thread



def getImgLabel(path):
    path_data = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    uids = []
    for img_path in path_data:
        raw_img = Image.open(img_path).convert('L')
        img_np = np.array(raw_img,'uint8')
        uid = int(os.path.split(img_path)[-1].split(".")[1])
        faces.append(img_np)
        uids.append(uid)    
    return faces, uids

def count_img(path):
    path_data = [os.path.join(path,f) for f in os.listdir(path)]
    img_counter = 1
    for img_path in path_data:
        print(str(img_counter) + " Images trained ")
        time.sleep(0.005)
        img_counter += 1

def train_data():
    recog = cv2.face_LBPHFaceRecognizer.create()

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces, uids = getImgLabel("trainingdata")

    Thread(recog.train(faces,np.array(uids))).start()

    Thread(target = count_img("trainingdata")).start()

    recog.save("traindata"+os.sep+"train.yml")

    print("done task")

train_data()
# count_img("trainingdata")
# getImgLabel("trainingdata")