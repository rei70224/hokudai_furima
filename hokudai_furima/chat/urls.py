from django.conf.urls import url
from . import views

app_name = "chat"

urlpatterns = [
        url(r'^post/$', views.post_talk, name='post_talk'),
        #url(r'^details/(?P<pk>\d+)/$', views.product_details, name='product_details'),
    ]
