from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout_view),
    url(r'^user/update$', views.userUpdate, name="user_update"),
    url(r'^user/create$', views.userCreate, name="user_create"),
    url(r'^user/delete/(?P<user_id>[0-9]+)/$', views.userDelete, name = 'user_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)