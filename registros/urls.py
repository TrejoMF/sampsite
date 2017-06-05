from django.conf.urls import url
from views import DisplayRegisterView, Detail, List, Nuevo

urlpatterns = [
    url(r'^registro/$', DisplayRegisterView.as_view(), name='registro'),
    url(r'^detalle/(?P<pk>\d+)/$', Detail.as_view(), name='detalle'),
    url(r'^lista/$', List.as_view(), name='lista'),
    url(r'^nuevo/$', Nuevo.as_view(), name='nuevo'),
]
