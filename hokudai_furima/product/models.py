from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import F, Max, Q
from versatileimagefield.fields import PPOIField, VersatileImageField
import os
from versatileimagefield.placeholder import OnDiscPlaceholderImage

class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    image0 = VersatileImageField(
        '',
        upload_to='product', 
        blank=False,
        null=True
    )
    image1 = VersatileImageField(
        '',
        upload_to='product',
        blank=True,
    )
    image2 = VersatileImageField(
        '',
        upload_to='product',
        blank=True,
    )
    image3 = VersatileImageField(
        '',
        upload_to='product',
        blank=True,
    )
    wanting_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wanting_users')

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @property
    def image0_thumbnail_url(self):
        if self.image0 and hasattr(self.image0, 'url'):
            return self.image0.thumbnail['600x600'].url



