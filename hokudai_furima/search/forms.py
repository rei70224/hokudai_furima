from django import forms

class SearchProductForm(forms.Form):
    q = forms.CharField(label="検索ワード")
