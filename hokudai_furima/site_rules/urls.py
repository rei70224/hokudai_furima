from django.urls import path
from . import views

app_name = "site_rules"

urlpatterns = [
    path('privacy', views.privacy_policy, name='privacy_policy'),
    path('tos', views.tos, name='tos'),
]
