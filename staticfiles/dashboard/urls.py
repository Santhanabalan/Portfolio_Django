from . import views
from django.urls import path
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cgpa/', views.cgpa, name='cgpa'),
    path('sgpa/', views.sgpa, name='sgpa'),
    path('gpp/', views.gpp, name='gpp'),
    path('404/', views.error404, name='404'),
]