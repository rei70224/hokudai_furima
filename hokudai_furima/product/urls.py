from django.conf.urls import url
from . import views

app_name = "product"

urlpatterns = [
        url(r'^create/$', views.create_product, name='create_product'),
        url(r'^update/(?P<product_pk>\d+)/$', views.update_product, name='update_product'),
        url(r'^details/(?P<pk>\d+)/$', views.product_details, name='product_details'),
    ]
