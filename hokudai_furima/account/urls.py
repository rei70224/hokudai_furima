from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
        url(r'^$',views.signup, name='signup'),
        url(r'^login$',views.login, name='login'),
        ]
