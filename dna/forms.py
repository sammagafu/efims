
from django.forms import ModelForm
from . models import BiologyPF180,PoliceForm113,BiologyPF180Report,PoliceForm113Report

class BiologyPF180Form(ModelForm):
    class Meta:
        model = BiologyPF180
        fields = '__all__'

class Police113form(ModelForm):
    class Meta:
        model = PoliceForm113
        fields = '__all__'

class BiologyPF180ReportForm(ModelForm):
    class Meta:
        model = BiologyPF180Report
        fields = '__all__'

class Police113ReportForm(ModelForm):
    class Meta:
        model  = PoliceForm113Report
        fields = '__all__'