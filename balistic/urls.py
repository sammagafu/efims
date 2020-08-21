from django.urls import path
from . import views
app_name = "ballistic"
urlpatterns = [
    path('', views.BallisticListView.as_view(), name='list'),
    path('create', views.CreateCase.as_view(), name='home'),
    path('<int:pk>', views.BallisticDetailView.as_view(), name='details'),
]
