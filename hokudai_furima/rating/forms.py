from django import forms
from .models import UserRating

class UserRatingForm(forms.Form):
    RATING_CHOICES = (
        ('bad', '悪い'),
        ('normal', '普通'),
        ('good', '良い'),
    )
    rating = forms.ChoiceField(label='評価', widget=forms.RadioSelect, choices=RATING_CHOICES)
