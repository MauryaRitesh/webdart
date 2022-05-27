import os
import model
#import scraper
import csv
import matplotlib.pyplot as plt


cwd = os.getcwd()
#print(cwd)

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


fileName = open("/home/ritesh/Desktop/webdart/model/users.txt", "r")
user = fileName.read()

#Scraping and downloading the images to .../user/ directory
#scraper.main(user)

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
    exp = model.expressions(os.path.join(pwd, file))
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
plt.savefig(os.path.join(cwd, 'home', 'static', 'home' , 'img/') + 'out.jpg')
#plt.show()

'''label_dict = {0:'Angry',1:'Disgust',2:'Fear',3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'}

data = open("data.txt", "r")
Lines = data.readlines()
  
count = 0
for line in Lines:
    count += 1
    if (line.strip() == "Sad"):
        pass
'''
