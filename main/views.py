from django.shortcuts import render
from main.forms import ContactForm
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
        cc1   = int(request.POST['cc1'])
        cg1   = int(request.POST['cg1'])
        cc2   = int(request.POST['cc2'])
        cg2   = int(request.POST['cg2'])
        cc3   = int(request.POST['cc3'])
        cg3   = int(request.POST['cg3'])
        cc4   = int(request.POST['cc4'])
        cg4   = int(request.POST['cg4'])
        cc5   = int(request.POST['cc5'])
        cg5   = int(request.POST['cg5'])
        cc6   = int(request.POST['cc6'])
        cg6   = int(request.POST['cg6'])
        sgpa= ((cc1*cg1)+(cc2*cg2)+(cc3*cg3)+(cc4*cg4)+(cc5*cg5)+(cc6*cg6))/(cc1+cc2+cc3+cc4+cc5+cc6)
        return render(request, 'main/sgpa.html', {"sgpa": sgpa})
    else:
        return render(request, 'main/sgpa.html')

@login_required(login_url='/accounts/login') 
def cgpa (request):
    if request.method == 'POST':
        sem1   = float(request.POST['sem1'])
        sem2   = float(request.POST['sem2'])
        sem3   = float(request.POST['sem3'])
        sem4   = float(request.POST['sem4'])
        sem5   = float(request.POST['sem5'])
        sem6   = float(request.POST['sem6'])
        sem7   = float(request.POST['sem7'])
        sem8   = float(request.POST['sem8'])
        cgpa= (sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8)/8
        return render(request, 'main/cgpa.html', {"cgpa": cgpa})
    else:
        return render(request, 'main/cgpa.html')

@login_required(login_url='/accounts/login') 
def gpp (request):
    if request.method == 'POST':
        name   = request.POST['cname']
        cid = request.POST['cid']
        if cid == 't':
            cat1   = float(request.POST['cat1'])
            cat2   = float(request.POST['cat2'])
            as1   = float(request.POST['as1'])
            as2   = float(request.POST['as2'])
            ese   = float(request.POST['ese'])
            tint = ((cat1+cat2)*0.4)+((as1+as2)/2)
            theory = tint+(ese*0.4)
            avg= theory
        elif cid == 'l':
            cat1   = float(request.POST['cat1'])
            cat2   = float(request.POST['cat2'])
            as1   = float(request.POST['as1'])
            as2   = float(request.POST['as2'])
            ese   = float(request.POST['ese'])
            tint = ((cat1+cat2)*0.4)+((as1+as2)/2)
            theory = tint+(ese*0.4)
            lint   = float(request.POST['lbi'])
            lese   = float(request.POST['lese'])
            lab = lint + (lese*0.4)
            avg=((3*theory)+lab)/4
        else :
            avg='T'

        if avg>=90 and avg<=100:
            Grade = 'O'
        elif avg>=80 and avg<90:
            Grade = 'A+'
        elif avg>=70 and avg<80:
            Grade = 'A'
        elif avg>=60 and avg<70:
            Grade = 'B+'
        elif avg>=50 and avg<60:
            Grade = 'B'
        elif avg<50:
            Grade = 'RA'
        else:
            Grade = 'Error'
        context = {'Grade': Grade,'name':name}
        return render(request, 'main/gpp.html', context)
    else:
        return render(request, 'main/gpp.html')

@login_required(login_url='/accounts/login') 
def temp (request):
    return render(request, 'main/temp.html')

def handle_not_found (request,exception):
    return render(request, 'main/404.html')