from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('certificates/', views.certificates, name='certificates'),
    path('portfolio-details/<str:pk>/', views.portfolio_details, name='portfolio-details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cgpa/', views.cgpa, name='cgpa'),
    path('sgpa/', views.sgpa, name='sgpa'),
]