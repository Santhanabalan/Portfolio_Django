from django.forms import ModelForm
from main.models import Cgpa, Sgpa, Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CgpaForm(ModelForm):
    class Meta:
        model = Cgpa
        fields = '__all__'

class SgpaForm(ModelForm):
    class Meta:
        model = Sgpa
        fields = '__all__'