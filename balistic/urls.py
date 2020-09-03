from django.urls import path
from . import views
app_name = "ballistic"
urlpatterns = [
    path('', views.BallisticListView.as_view(), name='list'),
    path('report',views.ReportCreate.as_view(),name='report'),
    path('create', views.CreateCase.as_view(), name='home'),
    path('<int:pk>', views.BallisticDetailView.as_view(), name='details'),
    path('<int:pk>/delete', views.BallisticDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', views.BallisticUpdate.as_view(), name='update'),
]
