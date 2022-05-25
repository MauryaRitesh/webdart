from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests
#from .forms import NameForm
#from hello.home.models import Contact
from home.models import Contact

def index(request):
    context = {'variable': 'this is sent'}
    
    return render(request,'index.html',context)
    #return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")
def contact(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        number = request.POST.get('number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        code = request.POST.get('code')
        contact = Contact(requests.POST) 
        contact.save()
        messages.success(requests,'Your Message has been sent')
    return render(request,'contact.html')           


#def contact(request):
#    if request.method == "POST":
#       form = NameForm(request.POST)
#       
#       if form.is_valid():
#            contact_f = Contact(request.POST)
#            contact_f.save() 
#            messages.success(request, 'Your Message has been sent')
#    else:
#        form = NameForm()
#
#    return render(request, 'contact.html', {'form': form})


