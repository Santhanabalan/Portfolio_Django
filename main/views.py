from django.shortcuts import render
from main.forms import ContactForm,CgpaForm,SgpaForm
from allauth.account.decorators import login_required

def index (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/index.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/index.html', context)

def certificates (request): 
    return render(request, 'main/certificates.html')

def portfolio (request): 
    return render(request, 'main/portfolio-details.html')

@login_required(login_url='/accounts/login') 
def dashboard (request):
    return render(request, 'main/dashboard.html')

@login_required(login_url='/accounts/login') 
def sgpa (request):
    if request.method == 'POST':
        form = SgpaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/sgpa.html')
    # else:
    #     user = user_display
    #     form = SgpaForm(initial={'name': user})
    form = SgpaForm()
    context = {'form': form}
    return render(request, 'main/sgpa.html',context)

@login_required(login_url='/accounts/login') 
def cgpa (request):
    if request.method == 'POST':
        form = CgpaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/cgpa.html')
    form = CgpaForm()
    context = {'form': form}
    return render(request, 'main/cgpa.html',context)

@login_required(login_url='/accounts/login') 
def gpp (request):
    return render(request, 'main/gpp.html')

@login_required(login_url='/accounts/login') 
def temp (request):
    return render(request, 'main/temp.html')

def handle_not_found (request,exception):
    return render(request, 'main/404.html')