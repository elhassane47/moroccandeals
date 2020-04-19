from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'deals/(?P<slug>[a-z0-9-_]+?)-(?P<deal_id>[0-9]+)/$',
        views.deal_details, name='deal-detail'),
    url('^deals/add', views.create_deal, name='deal-create'),
    url('^deals/all', views.DealsList.as_view(), name='deals-list'),
    url('', views.Home.as_view(), name='home'),

]