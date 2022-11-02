from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('profile/',TemplateView.as_view(template_name='account/profile.html'), name='profile'),
    path('accounts/', include('allauth.urls')),
]

handler404 ="main.views.handle_not_found"
handler500 ="main.views.error_500"
handler403 ="main.views.handle_not_found"
handler400 ="main.views.handle_not_found"