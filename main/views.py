from django.shortcuts import render
from .forms import ContactForm
from .models import Project,Certificate
# Create your views here.
def index (request):
    projects=Project.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/index.html')
    form = ContactForm()
    context = {'projects':projects,'form': form}
    return render(request, 'main/index.html', context)

def certificates (request):
    certificates=Certificate.objects.all()
    context = {'certificates':certificates}
    return render(request, 'main/certificates.html', context)

def portfolio_details (request): 
    return render(request, 'main/portfolio-details.html')