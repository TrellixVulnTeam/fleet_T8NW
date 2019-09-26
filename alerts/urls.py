from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import alert_function




urlpatterns = [
    path('alerts/', alert_function, name='alerts'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)