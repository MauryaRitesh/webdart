from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import requests
import csv
from .forms import NameForm, Profile, ContactForm
from home.models import Contact
import os

def index(request):
    form = Profile()
    if request.method == 'POST':
        form = Profile(request.POST)
        if form.is_valid():
            file = '/home/ritesh/Desktop/webdart/model/users.txt'
            with open(file, 'w') as f:
                user = form.cleaned_data['name']
                f.write(user)
            command = "instagram-scraper -f {} -u chesislub -p abcd4321 -m 10 -t image".format(file)
            os.system(command)
            os.system("python3 /home/ritesh/Desktop/webdart/model/main.py")
            return render(request,'result.html')


    context = {'form': form}
    
    return render(request,'index.html',context)
    #return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")
def result(request):
    return render(request,'result.html')
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")
'''def contact(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        number = request.POST.get('number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        code = request.POST.get('code')
        contact = Contact(request.POST) 
        contact.save()
        messages.success(request,'Your Message has been sent')
    return render(request,'contact.html')           
'''

def contact(request):

    form = ContactForm()
    if request.method == "POST":
       form = ContactForm(request.POST)
       print(form.is_valid())
       '''for field in form:
           print("Field Error: ", field.name, field.errors)'''
       
       if form.is_valid():
            #contact_f = Contact(request.POST)
            form.save() 
            messages.success(request, 'Your Message has been sent')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def profile(request):
    if request.method == "POST":
       form = Profile(request.POST)
       print (form.is_valid())
       if form.is_valid():
           name = form.cleaned_data['name']
           with open('data.txt', 'w') as file:
                file.write(name)
    else:
        form = Profile()

    return render(request, 'result.html', {'form': form})