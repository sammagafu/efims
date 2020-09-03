from django.forms import ModelForm
from . models import Ballistic, BallisticReport

class BallisticForm(ModelForm):
    class Meta:
        model = Ballistic
        fields = ['yourref','ourref','station','article','examination','addition','deliver']


class BallisticReportForm(ModelForm):
    
    class Meta:
        model = BallisticReport
        fields = ['report']
