from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from avishek.views import sendemail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sendemail,name='email'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
