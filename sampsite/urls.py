from django.conf.urls import url
from django.contrib import admin
from sampsite.views import *
from django.conf.urls import include

urlpatterns = [
    # Url principal
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),

    # Url's incluidas
    url(r'^', include('polls.urls')),
    url(r'^', include('registros.urls')),
]
