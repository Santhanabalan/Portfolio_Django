from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('home/',TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
]