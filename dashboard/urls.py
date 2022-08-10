from . import views
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('404/', views.error, name='404'),
    path('blank/', views.blank, name='blank'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('utilities_animation/', views.utilities_animation, name='utilities_animation'),
    path('utilities_border/', views.utilities_border, name='utilities_border'),
    path('utilities_color/', views.utilities_color, name='utilities_color'),
    path('utilities_other/', views.utilities_other, name='utilities_other'),

]