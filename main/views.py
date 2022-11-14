from django.shortcuts import render
from main.forms import ContactForm
from allauth.account.decorators import login_required
from itertools import islice
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, date
from django.contrib.admin.views.decorators import staff_member_required

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
        cid = request.POST['cid']
        if cid == '5':
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
            tsgpa= ((cc1*cg1)+(cc2*cg2)+(cc3*cg3)+(cc4*cg4)+(cc5*cg5))/(cc1+cc2+cc3+cc4+cc5)
            sgpa = round(tsgpa, 2)
        elif cid == '6':
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
            tsgpa= ((cc1*cg1)+(cc2*cg2)+(cc3*cg3)+(cc4*cg4)+(cc5*cg5)+(cc6*cg6))/(cc1+cc2+cc3+cc4+cc5+cc6)
            sgpa = round(tsgpa, 2)
        elif cid == '7':
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
            cc7   = int(request.POST['cc7'])
            cg7   = int(request.POST['cg7'])
            tsgpa= ((cc1*cg1)+(cc2*cg2)+(cc3*cg3)+(cc4*cg4)+(cc5*cg5)+(cc6*cg6)+(cc7*cg7))/(cc1+cc2+cc3+cc4+cc5+cc6+cc7)
            sgpa = round(tsgpa, 2)

        else :
            sgpa="Error"
        
        return render(request, 'main/sgpa.html', {"sgpa": sgpa})
    else:
        return render(request, 'main/sgpa.html')

@login_required(login_url='/accounts/login') 
def cgpa (request):
    if request.method == 'POST':
        cdata = request.POST.items()
        data = list(cdata)
        data.pop(0)
        a = [float(i[1]) for i in data]
        cgpat = sum(a) / len(a)
        cgpa = round(cgpat, 2)
            
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

def error_500 (request):
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
        cc41   = int(request.POST['cc41'])
        cg41   = int(request.POST['cg41'])
        cc42   = int(request.POST['cc42'])
        cg42   = int(request.POST['cg42'])
        cc43   = int(request.POST['cc43'])
        cg43   = int(request.POST['cg43'])
        cc44   = int(request.POST['cc44'])
        cg44   = int(request.POST['cg44'])
        cc45   = int(request.POST['cc45'])
        cg45   = int(request.POST['cg45'])
        cc46   = int(request.POST['cc46'])
        cg46   = int(request.POST['cg46'])
        tise= ((cc11*cg11)+(cc12*cg12)+(cc13*cg13)+(cc14*cg14)+(cc15*cg15)+(cc16*cg16)+(cc21*cg21)+(cc22*cg22)+(cc23*cg23)+(cc24*cg24)+(cc25*cg25)+(cc26*cg26)+(cc31*cg31)+(cc32*cg32)+(cc33*cg33)+(cc34*cg34)+(cc35*cg35)+(cc41*cg41)+(cc42*cg42)+(cc43*cg43)+(cc44*cg44)+(cc45*cg45)+(cc46*cg46))/(cc11+cc12+cc13+cc14+cc15+cc16+cc21+cc22+cc23+cc24+cc25+cc26+cc31+cc32+cc33+cc34+cc35+cc41+cc42+cc43+cc44+cc45+cc46)
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
        cc41   = int(request.POST['cc41'])
        cg41   = int(request.POST['cg41'])
        cc42   = int(request.POST['cc42'])
        cg42   = int(request.POST['cg42'])
        cc43   = int(request.POST['cc43'])
        cg43   = int(request.POST['cg43'])
        cc44   = int(request.POST['cc44'])
        cg44   = int(request.POST['cg44'])
        cc45   = int(request.POST['cc45'])
        cg45   = int(request.POST['cg45'])
        cc46   = int(request.POST['cc46'])
        cg46   = int(request.POST['cg46'])
        cc47   = int(request.POST['cc47'])
        cg47   = int(request.POST['cg47'])
        tise= ((cc11*cg11)+(cc12*cg12)+(cc13*cg13)+(cc14*cg14)+(cc15*cg15)+(cc16*cg16)+(cc21*cg21)+(cc22*cg22)+(cc23*cg23)+(cc24*cg24)+(cc25*cg25)+(cc26*cg26)+(cc31*cg31)+(cc32*cg32)+(cc33*cg33)+(cc34*cg34)+(cc35*cg35)+(cc36*cg36)+(cc41*cg41)+(cc42*cg42)+(cc43*cg43)+(cc44*cg44)+(cc45*cg45)+(cc46*cg46))/(cc11+cc12+cc13+cc14+cc15+cc16+cc21+cc22+cc23+cc24+cc25+cc26+cc31+cc32+cc33+cc34+cc35+cc36+cc41+cc42+cc43+cc44+cc45+cc46+cc47)
        ise = round(tise, 2)
        return render(request, 'main/ise1.html', {"ise": ise})
    else:
        return render(request, 'main/ise1.html')

@staff_member_required
def outpass(request):
    if request.method == "POST":
        ttime = request.POST['time']
        d = datetime.strptime(ttime, "%H:%M")
        time = d.strftime("%I:%M %p")
        today = date.today()
        date1 = today.strftime("%Y-%m-%d")
        context = {'date': date1,'time':time}
        subject = 'Outing Request Approved - Santhanabalan V 20BIS038'
        html_message = render_to_string('main/outpasstemplate.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'hostelkct2@outlook.com'
        to = 'santhanabalan.20is@kct.ac.in'
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        return render(request, 'main/outpass_form.html')
    else:
        return render(request, 'main/outpass_form.html')

def onichans(request):
    if request.method == "POST":
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        ttime = request.POST['time']
        d = datetime.strptime(ttime, "%H:%M")
        time = d.strftime("%I:%M %p")
        today = date.today()
        date1 = today.strftime("%Y-%m-%d")
        context = {'date': date1,'time':time, 'name':name}
        subject = f'Outing Request Approved - {name} {roll}'
        html_message = render_to_string('main/onichanstemplate.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'hostelkct2@outlook.com'
        to = email
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        return render(request, 'main/onichans.html')
    else:
        return render(request, 'main/onichans.html')