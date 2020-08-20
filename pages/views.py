from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from . forms import ClientForm
from . models import Client


class Homepage(LoginRequiredMixin, TemplateView):
    template_name = "registration/index.html"

# Create your views here.
class CreateClient(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class = ClientForm
    model = Client
    template_name ="clients/create.html"

class ClientList(LoginRequiredMixin,ListView):
    model = Client
    context_object_name = 'client'
    template_name ="clients/list.html"

class ClientDetail(LoginRequiredMixin,DetailView):
    model = Client
    context_object_name = 'client'
    template_name ="clients/detail.html"
