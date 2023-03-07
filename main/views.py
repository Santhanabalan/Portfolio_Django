from django.shortcuts import render

# Create your views here.
def index (request): 
    return render(request, 'main/index.html')

def certificates (request): 
    return render(request, 'main/certificates.html')

def portfolio_details (request): 
    return render(request, 'main/portfolio-details.html')