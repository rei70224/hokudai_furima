from django import forms

class SearchProductForm(forms.Form):
    PRICE_RANGE_OPTIONS = (('0_1000000', '全て'), ('0_1000','0 ~ 1000'), ('1000_3000', '1000 ~ 3000'), ('3000_5000', '3000 ~ 5000'), ('5000_10000', '5000 ~ 10000'), ('10000_1000000', '10000 ~ '))
    q = forms.CharField(label="検索ワード")
    price_range = forms.ChoiceField(label="価格帯", choices=PRICE_RANGE_OPTIONS)
    is_sold = forms.ChoiceField(label="販売中/売り切れ", choices=(('all', '全て'), ('sold_out', '売り切れ'), ('not_sold', '販売中')))
