from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MatchingOffer, MatchingOfferTalk

# Create your views here.
@login_required
def matching_offer_details(request, pk):
    matching_offer = get_object_or_404(MatchingOffer, pk=pk)
    talks = MatchingOfferTalk.objects.filter(matching_offer=matching_offer)
    return render(request, 'matching_offer/matching_offer_details.html', {'matching_offer': matching_offer, 'talks': talks})
