from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import BiologyPF180,PoliceForm113
from . forms import BiologyPF180Form, Police113form


# Create your views here.

class BiologyListView(LoginRequiredMixin,ListView):
    model = BiologyPF180
    context_object_name = "dna"
    template_name = "dna/biology-list.html"

class BiologyDetail(LoginRequiredMixin,DetailView):
    model = BiologyPF180
    context_object_name = 'dna'
    template_name = "dna/biology-details.html"

class BiologyCreate(LoginRequiredMixin,CreateView):
    model = BiologyPF180
    form_class = BiologyPF180Form
    template_name = "dna/create.html"

# form 113 police

class Policeform113List(LoginRequiredMixin,ListView):
    model = PoliceForm113
    context_object_name = "dna"
    template_name = "dna/police113-list.html"


class Policeform113Detail(LoginRequiredMixin,DetailView):
    model = PoliceForm113
    context_object_name = "dna"
    template_name = "dna/police113-detail.html"

class PoliceForm113Create(LoginRequiredMixin,CreateView):
    model = PoliceForm113
    form_class = Police113form
    template_name = "dna/police113-create.html"
    