from tensorflow import keras
import cv2
import numpy as np
model = keras.models.load_model('model.h5')

def facecrop(image):
    ## Crops the face of a person from any image!

    ## OpenCV XML FILE for Frontal Facial Detection using HAAR CASCADES.
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)

    ## Reading the given Image with OpenCV
    img = cv2.imread(image)

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


    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    #img = facecrop(file)
    img = cv2.resize(img, (48,48))
    img = np.array(img)

    img = np.expand_dims(img,axis = 0) #makes image shape (1,48,48)
    img = img.reshape(1,48,48,1)
    result = model.predict(img)
    result = list(result[0])
    print(result)

    img_index = result.index(max(result))
    print(label_dict[img_index])


if __name__ == "__main__":
    expressions("/home/archi/Desktop/2.jpg")