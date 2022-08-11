from django.shortcuts import render
from main.forms import ContactForm

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

def dashboard (request):
    return render(request, 'main/dashboard.html')

def sgpa (request):
    return render(request, 'main/sgpa.html')

def cgpa (request):
    return render(request, 'main/cgpa.html')

def gpp (request):
    return render(request, 'main/gpp.html')

def temp (request):
    return render(request, 'main/temp.html')

def handle_not_found (request,exception):
    return render(request, 'main/temp.html')