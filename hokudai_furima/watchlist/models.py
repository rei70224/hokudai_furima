from django.db import models
from hokudai_furima.product.models import Product
from django.conf import settings
from django.utils import timezone

# Create your models here.
class WatchList(models.Model):
    products = models.ManyToManyField(Product, related_name='watchlist_product')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='watching_user')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()
