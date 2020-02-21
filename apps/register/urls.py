from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout_view),
    url(r'^user/update$', views.userUpdate, name="user_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)