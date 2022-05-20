from django.shortcuts import render
from projects.models import Project
from django.core.files.storage import FileSystemStorage
import requests, json 

url =  "http://127.0.0.1:8000/api/image/" 

def post():
    image = '/home/archi/Desktop/1.jpg'
    files = {'file': open(image, 'rb') }
    response = requests.post(url, files=files)
            #print(response.text)
    with open('data.txt', 'w') as output:
        output.write(response.text)

def upload(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    if request.method == 'POST':
        #post()
        upload = request.FILES.getlist('upload')
        post()
            
        
        #return render(request, 'result.html')
    return render(request, 'upload.html')

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)



def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def result(request):
    with open('data.txt','r') as file:
        #list to return
        to_return = []
        a = file.readlines()

        for tab in a:
            tab = tab.split() #this "divides" the columns 
            #then just append the third column
            to_return.append(tab[2])

    return render(request, 'result.html')
