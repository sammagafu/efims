from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Ballistic
from . forms import BallisticForm
# Create your views here.

class CreateCase(LoginRequiredMixin,CreateView):
    form_class = BallisticForm
    model = Ballistic
    template_name = "ballistic/create.html"

    def form_valid(self, form):
        form.instance.receicer = self.request.user
        return super().form_valid(form)

class BallisticDetailView(LoginRequiredMixin,DetailView):
    model = Ballistic
    object_context_name = "ballistic"
    template_name = "ballistic/detail.html"


class BallisticListView(LoginRequiredMixin,ListView):
    context_object_name = 'cases'
    model = Ballistic
    template_name = "ballistic/list.html"


class BallisticDeleteView(DeleteView):
    model = Ballistic
    success_url = "/ballistic"
    template_name = "ballistic/delete.html"

class BallisticUpdate(UpdateView):
    form_class = BallisticForm
    model = Ballistic
    template_name = "ballistic/update.html"