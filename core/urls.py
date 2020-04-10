from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^(?P<slug>[a-z0-9-_]+?)-(?P<deal_id>[0-9]+)/$',
        views.deal_details, name='deal-detail'),
    url('', views.DealsList.as_view(), name='deals-list'),

]