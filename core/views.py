from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from core.models import Deal


def deal_details(request, slug, deal_id, form=None):
    pass


class DealsList(ListView):
    model = Deal
    paginate_by = 20

