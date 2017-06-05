from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models


class poll(models.Model):
    Nombre = models.CharField(max_length=200, null=True, blank=True)
    Apellido = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField()
    FechaCreacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    FechaModificacion = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.Nombre, ' ', self.Apellido)
