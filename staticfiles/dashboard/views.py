from django.shortcuts import render
from allauth.account.decorators import login_required

@login_required(login_url='/accounts/login') 
def dashboard (request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='/accounts/login') 
def cgpa (request):
    return render(request, 'dashboard/cgpa.html')

@login_required(login_url='/accounts/login') 
def sgpa (request):
    return render(request, 'dashboard/sgpa.html')

@login_required(login_url='/accounts/login') 
def gpp (request):
    return render(request, 'dashboard/gpp.html')

@login_required(login_url='/accounts/login') 
def error404 (request):
    return render(request, 'dashboard/404.html')