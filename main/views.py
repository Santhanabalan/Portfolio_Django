import email
from django.shortcuts import render
from .forms import ContactForm

def home (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/home.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/home.html', context)

def certificates (request): 
    return render(request, 'main/certificates.html')

def portfoliod (request): 
    return render(request, 'main/portfolio-details.html')

def speed (request): 
    return render(request, 'main/speed.html')
