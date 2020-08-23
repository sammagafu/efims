from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import BiologyPF180,PoliceForm113


# Create your views here.

class BiologyListView(LoginRequiredMixin,ListView):
    model = BiologyPF180
    object_context_name = "dna"
    template_name = "dna/biology-list.html"

class BiologyDetail(LoginRequiredMixin,DetailView):
    model = BiologyPF180
    object_context_name = "dna"
    template_name = "dna/biology-details.html"
