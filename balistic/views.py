from django.shortcuts import render
from django.views.generic import CreateView
from . models import Ballistic
from . forms import BallisticForm
# Create your views here.

class CreateCase(CreateView):
    form_class = BallisticForm
    model = Ballistic
    template_name = "ballistic/create.html"
