from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('certificates.html', views.certificates, name='certificates'),
    path('portfolio-details.html', views.portfoliod, name='portfoliod'),
    path('speed.html', views.speed, name='speed'),
]