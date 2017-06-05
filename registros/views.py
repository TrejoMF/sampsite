from django.shortcuts import render, get_object_or_404
from .models import registro
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


class Detail(DetailView):
    model = registro
    template_name = "detail.html"

    def get(self, request, pk, **kwargs):
        producto = get_object_or_404(self.model, pk=pk)
        context = {
            "objeto": producto
        }
        return render(request, self.template_name, context)


class DisplayRegisterView(TemplateView):
    template_name = 'registro.html'
