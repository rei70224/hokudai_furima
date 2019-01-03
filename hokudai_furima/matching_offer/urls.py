from django.urls import path, re_path
from . import views

app_name = "matching_offer"

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.matching_offer_details, name='matching_offer_details'),
    #path('create', views.create_matching_offer, name='create_matching_offer'),
    #re_path(r'^update/(?P<matching_offer_pk>\d+)/$', views.update_matching_offer, name='update_matching_offer'),
]
