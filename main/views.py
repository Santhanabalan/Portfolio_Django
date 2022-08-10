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

def speed (request): 
    return render(request, 'main/speed.html')
def dashboard (request):
    return render(request, 'main/dashboard.html')

def login (request): 
    return render(request, 'main/login.html')

def register (request): 
    return render(request, 'main/register.html')

def forgotpassword (request): 
    return render(request, 'main/forgot-password.html')

def blank (request): 
    return render(request, 'main/blank.html')

def buttons (request): 
    return render(request, 'main/buttons.html')

def cards (request): 
    return render(request, 'main/cards.html')

def charts (request): 
    return render(request, 'main/charts.html')

def tables (request): 
    return render(request, 'main/tables.html')

def utilities_animation (request): 
    return render(request, 'main/utilities-animation.html')

def utilities_border (request): 
    return render(request, 'main/utilities-border.html')

def utilities_color (request): 
    return render(request, 'main/utilities-color.html')

def utilities_other (request): 
    return render(request, 'main/utilities-color.html')

def error (request): 
    return render(request, 'main/404.html')
