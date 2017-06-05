from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class registro(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        view_name = 'detalle'
        return reverse(view_name, kwargs={"pk": self.id})
