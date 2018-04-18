from django import forms

from .models import Product

class NewProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'price',  'image0', 'image1', 'image2', 'image3')

    def __init__(self, *args, **kwargs):
        super(NewProductForm, self).__init__(*args, **kwargs)
        for i in range(4):
            self.fields['image'+str(i)].widget.attrs={'style':'display:none;', 'id':'file_'+str(i) , 'onchange': 'fileget(this,\''+str(i)+'\');', }

class UpdateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'is_sold')

