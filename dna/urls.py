# from django.urls import path
from django.urls import path
from . import views
app_name = 'dna'
urlpatterns = [
    path('biology/', views.BiologyListView.as_view(), name='list'),
    path('biology/<int:pk>', views.BiologyDetail.as_view(), name='detail'),
    path('biology/create', views.BiologyCreate.as_view(), name='create'),
    # form 113
    path('police113/',views.Policeform113List.as_view(),name="police-list"),
    path('police113/<int:pk>',views.Policeform113Detail.as_view(),name="police-detail"),
    path('police113/create',views.PoliceForm113Create.as_view(),name="police-create"),
]
