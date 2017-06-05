from django.shortcuts import render
from django.views.generic import TemplateView


class DisplayTaskView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        data = {
            'nombre': 'francisco',
            'apellido': 'trejo'
        }
        return render(request, self.template_name, data)
