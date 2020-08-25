from django.urls import path
from . import views
urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('client/create', views.CreateClient.as_view(), name='create-client'),
    path('client/', views.ClientList.as_view(), name='list-client'),
    path('client/<int:pk>', views.ClientDetail.as_view(), name='list-detail'),
    path('client/<int:pk>/delete', views.ClientDeleteView.as_view(), name='delete-client'),
    path('client/<int:pk>/update', views.ClientUpdateView.as_view(), name='update-client'),

]
