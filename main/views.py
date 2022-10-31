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

@login_required(login_url='/accounts/login') 
def ise (request):
    if request.method == 'POST':
        cc11   = int(request.POST['cc11'])
        cg11   = int(request.POST['cg11'])
        cc12   = int(request.POST['cc12'])
        cg12   = int(request.POST['cg12'])
        cc13   = int(request.POST['cc13'])
        cg13   = int(request.POST['cg13'])
        cc14   = int(request.POST['cc14'])
        cg14   = int(request.POST['cg14'])
        cc15   = int(request.POST['cc15'])
        cg15   = int(request.POST['cg15'])
        cc16   = int(request.POST['cc16'])
        cg16   = int(request.POST['cg16'])
        cc21   = int(request.POST['cc21'])
        cg21   = int(request.POST['cg21'])
        cc22   = int(request.POST['cc22'])
        cg22   = int(request.POST['cg22'])
        cc23   = int(request.POST['cc23'])
        cg23   = int(request.POST['cg23'])
        cc24   = int(request.POST['cc24'])
        cg24   = int(request.POST['cg24'])
        cc25   = int(request.POST['cc25'])
        cg25   = int(request.POST['cg25'])
        cc26   = int(request.POST['cc26'])
        cg26   = int(request.POST['cg26'])
        cc31   = int(request.POST['cc31'])
        cg31   = int(request.POST['cg31'])
        cc32   = int(request.POST['cc32'])
        cg32   = int(request.POST['cg32'])
        cc33   = int(request.POST['cc33'])
        cg33   = int(request.POST['cg33'])
        cc34   = int(request.POST['cc34'])
        cg34   = int(request.POST['cg34'])
        cc35   = int(request.POST['cc35'])
        cg35   = int(request.POST['cg35'])
        cc36   = int(request.POST['cc36'])
        cg36   = int(request.POST['cg36'])
        tise= ((cc11*cg11)+(cc12*cg12)+(cc13*cg13)+(cc14*cg14)+(cc15*cg15)+(cc16*cg16)+(cc21*cg21)+(cc22*cg22)+(cc23*cg23)+(cc24*cg24)+(cc25*cg25)+(cc26*cg26)+(cc31*cg31)+(cc32*cg32)+(cc33*cg33)+(cc34*cg34)+(cc35*cg35)+(cc36*cg36))/(cc11+cc12+cc13+cc14+cc15+cc16+cc21+cc22+cc23+cc24+cc25+cc26+cc31+cc32+cc33+cc34+cc35+cc36)
        ise = round(tise, 2)
        return render(request, 'main/ise.html', {"ise": ise})
    else:
        return render(request, 'main/ise.html')

@login_required(login_url='/accounts/login') 
def ise1 (request):
    if request.method == 'POST':
        cc11   = int(request.POST['cc11'])
        cg11   = int(request.POST['cg11'])
        cc12   = int(request.POST['cc12'])
        cg12   = int(request.POST['cg12'])
        cc13   = int(request.POST['cc13'])
        cg13   = int(request.POST['cg13'])
        cc14   = int(request.POST['cc14'])
        cg14   = int(request.POST['cg14'])
        cc15   = int(request.POST['cc15'])
        cg15   = int(request.POST['cg15'])
        cc16   = int(request.POST['cc16'])
        cg16   = int(request.POST['cg16'])
        cc21   = int(request.POST['cc21'])
        cg21   = int(request.POST['cg21'])
        cc22   = int(request.POST['cc22'])
        cg22   = int(request.POST['cg22'])
        cc23   = int(request.POST['cc23'])
        cg23   = int(request.POST['cg23'])
        cc24   = int(request.POST['cc24'])
        cg24   = int(request.POST['cg24'])
        cc25   = int(request.POST['cc25'])
        cg25   = int(request.POST['cg25'])
        cc26   = int(request.POST['cc26'])
        cg26   = int(request.POST['cg26'])
        cc31   = int(request.POST['cc31'])
        cg31   = int(request.POST['cg31'])
        cc32   = int(request.POST['cc32'])
        cg32   = int(request.POST['cg32'])
        cc33   = int(request.POST['cc33'])
        cg33   = int(request.POST['cg33'])
        cc34   = int(request.POST['cc34'])
        cg34   = int(request.POST['cg34'])
        cc35   = int(request.POST['cc35'])
        cg35   = int(request.POST['cg35'])
        cc36   = int(request.POST['cc36'])
        cg36   = int(request.POST['cg36'])
        ec1 = int(request.POST['ec1'])
        eg1 = int(request.POST['eg1'])
        tise= ((cc11*cg11)+(cc12*cg12)+(cc13*cg13)+(cc14*cg14)+(cc15*cg15)+(cc16*cg16)+(cc21*cg21)+(cc22*cg22)+(cc23*cg23)+(cc24*cg24)+(cc25*cg25)+(cc26*cg26)+(cc31*cg31)+(cc32*cg32)+(cc33*cg33)+(cc34*cg34)+(cc35*cg35)+(cc36*cg36)+(ec1*eg1))/(cc11+cc12+cc13+cc14+cc15+cc16+cc21+cc22+cc23+cc24+cc25+cc26+cc31+cc32+cc33+cc34+cc35+cc36+ec1)
        ise = round(tise, 2)
        return render(request, 'main/ise.html', {"ise": ise})
    else:
        return render(request, 'main/ise.html')

@login_required(login_url='/accounts/login') 
def ise2 (request):
    if request.method == 'POST':
        cc11   = int(request.POST['cc11'])
        cg11   = int(request.POST['cg11'])
        cc12   = int(request.POST['cc12'])
        cg12   = int(request.POST['cg12'])
        cc13   = int(request.POST['cc13'])
        cg13   = int(request.POST['cg13'])
        cc14   = int(request.POST['cc14'])
        cg14   = int(request.POST['cg14'])
        cc15   = int(request.POST['cc15'])
        cg15   = int(request.POST['cg15'])
        cc16   = int(request.POST['cc16'])
        cg16   = int(request.POST['cg16'])
        cc21   = int(request.POST['cc21'])
        cg21   = int(request.POST['cg21'])
        cc22   = int(request.POST['cc22'])
        cg22   = int(request.POST['cg22'])
        cc23   = int(request.POST['cc23'])
        cg23   = int(request.POST['cg23'])
        cc24   = int(request.POST['cc24'])
        cg24   = int(request.POST['cg24'])
        cc25   = int(request.POST['cc25'])
        cg25   = int(request.POST['cg25'])
        cc26   = int(request.POST['cc26'])
        cg26   = int(request.POST['cg26'])
        cc31   = int(request.POST['cc31'])
        cg31   = int(request.POST['cg31'])
        cc32   = int(request.POST['cc32'])
        cg32   = int(request.POST['cg32'])
        cc33   = int(request.POST['cc33'])
        cg33   = int(request.POST['cg33'])
        cc34   = int(request.POST['cc34'])
        cg34   = int(request.POST['cg34'])
        cc35   = int(request.POST['cc35'])
        cg35   = int(request.POST['cg35'])
        cc36   = int(request.POST['cc36'])
        cg36   = int(request.POST['cg36'])
        ec1 = int(request.POST['ec1'])
        eg1 = int(request.POST['eg1'])
        ec2 = int(request.POST['ec2'])
        eg2 = int(request.POST['eg2'])
        tise= ((cc11*cg11)+(cc12*cg12)+(cc13*cg13)+(cc14*cg14)+(cc15*cg15)+(cc16*cg16)+(cc21*cg21)+(cc22*cg22)+(cc23*cg23)+(cc24*cg24)+(cc25*cg25)+(cc26*cg26)+(cc31*cg31)+(cc32*cg32)+(cc33*cg33)+(cc34*cg34)+(cc35*cg35)+(cc36*cg36)+(ec1*eg1)+(ec2*eg2))/(cc11+cc12+cc13+cc14+cc15+cc16+cc21+cc22+cc23+cc24+cc25+cc26+cc31+cc32+cc33+cc34+cc35+cc36+ec1+ec2)
        ise = round(tise, 2)
        return render(request, 'main/ise.html', {"ise": ise})
    else:
        return render(request, 'main/ise.html')

