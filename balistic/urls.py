from django.urls import path
from . import views
app_name = "ballistic"
urlpatterns = [
    path('', views.CreateCase.as_view(), name='home'),
]
