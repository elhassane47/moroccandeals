from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views.generic import View, TemplateView, ListView, DetailView
from core.models import Deal, Category


def deal_details(request, slug, deal_id, form=None):
    deal = get_object_or_404(Deal, pk=deal_id)

    context = {}

    context['object'] = deal
    context['more_deals'] = Deal.objects.filter(user=deal.user)[:3]
    return render(request, 'core/deal_detail.html', context)



class DealsList(ListView):
    model = Deal
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(DealsList, self).get_context_data(**kwargs)
        context['categories'] = Deal.objects.all().values('category__name').annotate(total=Count('category')).order_by('total')
        return context


# class DealDetail(DetailView):
#     model = Deal
def ledger1_detail_view(request, pk1, pk2):

    get_object_or_404(company, pk=pk1)
    ledger = get_object_or_404(ledger1, pk=pk2)

    context = {}
    context['ledger1_details'] = ledger
    # Add other items to the context
    ...

    return render(request, 'accounting_double_entry/ledger1_details.html', context)

