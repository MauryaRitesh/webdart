from tensorflow import keras
import cv2
import numpy as np
import os
import scraper
import csv
import matplotlib.pyplot as plt
model = keras.models.load_model('/home/ritesh/Desktop/webdart/model/model.h5')



def facecrop(image):
    ## Crops the face of a person from any image!

    ## OpenCV XML FILE for Frontal Facial Detection using HAAR CASCADES.
    facedata = "/home/ritesh/Desktop/webdart/model/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)

    ## Reading the given Image with OpenCV
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    try:
        ## Some downloaded images are of unsupported type and should be ignored while raising Exception, so for that
        ## we're using the try/except
    
        minisize = (img.shape[1],img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            sub_face = img[y:y+h, x:x+w]
            '''f_img = cv2.resize(sub_face, (48,48))

            f_name = image.split('/')
            f_name = f_name[-1]
            cv2.imwrite(f_name, f_img)'''

            return sub_face

    except:
        pass

def expressions(file):
    label_dict = {0:'Angry',1:'Disgust',2:'Fear',3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'}


    try:
        ## Sometimes, there isn't any face in the given image; hence img is empty
        #img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img = facecrop(file)
        img = cv2.resize(img, (48,48))
        img = np.array(img)

        img = np.expand_dims(img,axis = 0) #makes image shape (1,48,48)
        img = img.reshape(1,48,48,1)
        result = model.predict(img)
        result = list(result[0])
        print(result)

        img_index = result.index(max(result))
        print(label_dict[img_index])
        return label_dict[img_index]
    except:
        pass




cwd = os.getcwd()
print(cwd)

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


fileName = open("/home/ritesh/Desktop/webdart/model/users.txt", "r")
user = fileName.read()

#Scraping and downloading the images to .../user/ directory
scraper.main(user)

#new output file for new user
'''if os.path.exists(user + ".txt"):
    os.remove(user + ".txt")
'''
#for plotting
ang, dis, fer, hap, neu, sad, sur = 0, 0, 0 , 0, 0, 0, 0
pwd = os.path.join(cwd, user)
print( "User: ", user,"\nPWD: ", pwd)
for file in sorted(get_files(pwd)):
    print(os.path.join(pwd, file))
    exp = expressions(os.path.join(pwd, file))
    if (exp=="Angry"):
        ang += 1
    elif(exp=="Disgust"):
        dis += 1
    elif(exp=="Fear"):
        fer += 1
    elif(exp=="Happy"):
        hap += 1
    elif(exp=="Neutral"):
        neu += 1
    elif(exp=="Sad"):
        sad += 1
    elif(exp=="Surprise"):
        sur += 1
    with open(user + ".txt", 'a') as f:
        try:
            f.write(exp)
            f.write('\n')
        except:
            pass


data = {'Angry':ang, 'Disgust':dis,'Fear':fer, 'Happy':hap, 'Neutral':neu, 'Sad':sad, 'Surprise':sur}
exp = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(exp, values,
        width = 0.4)
 
plt.xlabel("Expressions")
plt.ylabel("No. of images")
plt.title("Expressions of {} from images.".format(user))
plt.savefig(os.path.join(cwd, 'home', 'static', 'home', 'img/') + 'out.jpg')
plt.show()

