from django.shortcuts import render
from django.db.models import Count
from django.views.generic import View, TemplateView, ListView, DetailView
from core.models import Deal, Category


def deal_details(request, slug, deal_id, form=None):
    pass


class DealsList(ListView):
    model = Deal
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(DealsList, self).get_context_data(**kwargs)
        context['categories'] = Deal.objects.all().values('category__name').annotate(total=Count('category')).order_by('total')
        return context


