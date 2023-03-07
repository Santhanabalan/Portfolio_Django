from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('certificates/', views.certificates, name='certificates'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
]