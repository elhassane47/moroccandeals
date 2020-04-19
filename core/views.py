from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import View, TemplateView, ListView, CreateView
from core.models import Deal, Category
from core.forms import DealCreate
from django.contrib.auth.decorators import login_required

class Home(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_deals'] = Deal.objects.all()[:6]

        return context

def deal_details(request, slug, deal_id, form=None):
    deal = get_object_or_404(Deal, pk=deal_id)

    context = {}

    context['object'] = deal
    context['more_deals'] = Deal.objects.filter(user=deal.user)[:3]
    return render(request, 'core/deal_detail.html', context)



@login_required
def create_deal(request):
    if request.method == 'POST':
        form = DealCreate(request.POST,request.FILES or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('deals:deals-list')
    else:
        form = DealCreate()
    return render(request, 'core/add_deal.html', {
        'form': form
    })

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

