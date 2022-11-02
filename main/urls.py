from main import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('certificates/', views.certificates, name='certificates'),
    path('portfolio-details/', views.portfolio, name='portfolio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sgpa/', views.sgpa, name='sgpa'),
    path('cgpa/', views.cgpa, name='cgpa'),
    path('gpp/', views.gpp, name='gpp'),
    path('temp/', views.temp, name='temp'),
    path('ise/', views.ise, name='ise'),
    path('ise0/', views.ise0, name='ise0'),
    path('ise1/', views.ise1, name='ise1'),
    path('ise2/', views.ise2, name='ise2'),
]