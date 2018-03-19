from django.conf.urls import url
from . import views

app_name = "product"

urlpatterns = [
        url(r'^new/$', views.create_product, name='create_product'),
        url(r'^details/(?P<pk>\d+)/$', views.product_details, name='product_details'),
    ]
