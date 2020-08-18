from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class Homepage(LoginRequiredMixin, TemplateView):
    template_name = "registration/index.html"

# Create your views here.