from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import F, Max, Q
from versatileimagefield.fields import PPOIField, VersatileImageField
import os
from versatileimagefield.placeholder import OnDiscPlaceholderImage

"""
class ProductImage(models.Model):
    image = VersatileImageField('Image',
        upload_to='products/images/', blank=False)
    #    upload_to='products/images/', ppoi_field='ppoi', blank=False)
    # image = VersatileImageField(
    #    'Image',
    #    upload_to='images/testimagemodel/',
    #    width_field='width',
    #    height_field='height'
    #)
    optional_image1 = VersatileImageField(
        'optional_image1',
        upload_to='products/images/',
        blank=True,
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.STATIC_URL,
                'placeholder.jpg'
            )
        )
    )
    optional_image2 = VersatileImageField(
        'optional_image2',
        upload_to='products/images/',
        blank=True,
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.STATIC_URL,
                'placeholder.jpg'
            )
        )
    )
    optional_image3 = VersatileImageField(
        'optional_image3',
        upload_to='products/images/',
        blank=True,
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.STATIC_URL,
                'placeholder.jpg'
            )
        )
    )

    #ppoi = PPOIField()
    alt = models.CharField(max_length=128, blank=True)
    order = models.PositiveIntegerField(editable=False)

    class Meta:
        ordering = ('order', )
        app_label = 'product'

    def get_ordering_queryset(self):
        return self.product.images.all()

    def save(self, *args, **kwargs):
        if self.order is None:
            qs = self.get_ordering_queryset()
            existing_max = qs.aggregate(Max('order'))
            existing_max = existing_max.get('order__max')
            self.order = 0 if existing_max is None else existing_max + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        qs = self.get_ordering_queryset()
        qs.filter(order__gt=self.order).update(order=F('order') - 1)
        super().delete(*args, **kwargs)
"""    
     
class Product(models.Model):
    IMAGE_DIR = 'img/product/'
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    #images = models.ForeignKey(ProductImage, related_name='images', on_delete=models.CASCADE, null=True)
    image0 = VersatileImageField('',
        upload_to=IMAGE_DIR,  blank=False, null=True)
        #upload_to='products/images/',  blank=False, null=True)

    image1 = VersatileImageField(
        '',
        upload_to=IMAGE_DIR,
        blank=True,
    )
    image2 = VersatileImageField(
        '',
        upload_to=IMAGE_DIR,
        blank=True,
    )
    image3 = VersatileImageField(
        '',
        upload_to=IMAGE_DIR,
        blank=True,
    )


    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




