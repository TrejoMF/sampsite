from django.conf.urls import url
from views import DisplayTaskView


urlpatterns = [
    url(r'^polls/$', DisplayTaskView.as_view(), name='index'),
]
