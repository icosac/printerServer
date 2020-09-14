from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('settings/', views.setting, name='setting'),
    path('settings/restart', views.restartServer, name='restartServer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
