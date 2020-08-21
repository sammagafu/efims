from django.forms import ModelForm
from . models import Ballistic

class BallisticForm(ModelForm):
    class Meta:
        model = Ballistic
        fields = '__all__'