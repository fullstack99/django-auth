from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', include('apps.register.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    url(r'^docs/$', get_swagger_view(title='API Docs'), name='api_docs')
]