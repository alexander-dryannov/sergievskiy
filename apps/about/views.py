from django.shortcuts import render
from django.views.generic import TemplateView

from apps.about import models


def get_contacts(request):
    return render(request, 'about/contact.html')


class DonateView(TemplateView):
    template_name = 'about/donate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requisites'] = models.Requisites.objects.last()
        return context


class ClergyView(TemplateView):
    template_name = 'about/clergy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clergy'] = models.Clergy.objects.all().order_by('pk')
        return context
