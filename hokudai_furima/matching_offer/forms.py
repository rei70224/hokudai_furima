from django import forms
from .models import MatchingOfferTalk


class MatchingOfferTalkForm(forms.ModelForm):
    class Meta:
        model = MatchingOfferTalk
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
