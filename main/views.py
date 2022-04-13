import email
from django.shortcuts import render

def home (request):
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        subject= request.POST['subject']
        message= request.POST['message']

        return render(request, 'main/home.html',{'name':name})
    else:
        return render(request, 'main/home.html')

def certificates (request): 
    return render(request, 'main/certificates.html')

def portfoliod (request): 
    return render(request, 'main/portfolio-details.html')

def speed (request): 
    return render(request, 'main/speed.html')
