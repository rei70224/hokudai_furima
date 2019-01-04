from django.db import models
from hokudai_furima.watchlist.models import WatchList
from django.utils import timezone
from django.conf import settings

# Create your models here.
class MatchingOffer(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=512)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, default=None)
    watchlist = models.ForeignKey(WatchList, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)


class MatchingOfferTalk(models.Model):
    talker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField('', max_length=512)
    matching_offer = models.ForeignKey(MatchingOffer, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)
