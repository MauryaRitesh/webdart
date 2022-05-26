import os
import model
import scraper
import csv

cwd = os.getcwd()

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

user = 'alia'
for file in sorted(get_files(cwd+'/'+user)):
    print(cwd+'/'+user+'/' + file)
    exp = model.expressions(cwd+'/'+user+'/' + file)
    with open('data.txt', 'a') as f:
        f.write(exp)
        f.write('\n')
    


