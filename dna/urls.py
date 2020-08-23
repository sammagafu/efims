from django.urls import path
from . import views
app_name = "dna"
urlpatterns = [
    path('', views.BiologyListView.as_view(), name='list'),
]
