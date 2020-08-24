
from django.forms import ModelForm
from . models import BiologyPF180,PoliceForm113

class BiologyPF180Form(ModelForm):
    class Meta:
        model = BiologyPF180
        fields = '__all__'

class Police113form(ModelForm):
    class Meta:
        model = PoliceForm113
        fields = '__all__'