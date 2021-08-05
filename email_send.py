import yagmail
import os

os.chdir("trainingdata")
file_data = sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
print(file_data[0])
yag_obj = yagmail.SMTP('technicaltraining73@gmail.com','Trainingtech321')
msg = "hey this is sample email"
yag_obj.send('ankitshukla172000@gmail.com','Test email Subject',msg,file_data)