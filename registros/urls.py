from django.conf.urls import url
from views import DisplayRegisterView, Detail

urlpatterns = [
    url(r'^registro/$', DisplayRegisterView.as_view(), name='registro'),
    url(r'^detalle/$', Detail.as_view(), name='detalle'),
]
