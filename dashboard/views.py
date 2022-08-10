from django.shortcuts import render

# Create your views here.
def dashboard (request):
    return render(request, 'dashboard/index.html')

def login (request): 
    return render(request, 'dashboard/login.html')

def register (request): 
    return render(request, 'dashboard/register.html')

def forgotpassword (request): 
    return render(request, 'dashboard/forgot-password.html')

def blank (request): 
    return render(request, 'dashboard/blank.html')

def buttons (request): 
    return render(request, 'dashboard/buttons.html')

def cards (request): 
    return render(request, 'dashboard/cards.html')

def charts (request): 
    return render(request, 'dashboard/charts.html')

def tables (request): 
    return render(request, 'dashboard/tables.html')

def utilities_animation (request): 
    return render(request, 'dashboard/utilities-animation.html')

def utilities_border (request): 
    return render(request, 'dashboard/utilities-border.html')

def utilities_color (request): 
    return render(request, 'dashboard/utilities-color.html')

def utilities_other (request): 
    return render(request, 'dashboard/utilities-color.html')

def error (request): 
    return render(request, 'dashboard/404.html')
