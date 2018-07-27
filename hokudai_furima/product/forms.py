from django import forms

from .models import Product, ProductImage

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'access_level')

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image',)

    def __init__(self, i, *args, **kwargs):
        super(ProductImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget = forms.FileInput()
        self.fields['image'].widget.attrs={'name':'image'+str(i), 'style':'display:none;', 'id':'file_'+str(i) , 'onchange': 'fileget(this,\''+str(i)+'\');', }

    @property
    def thumbnail_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.thumbnail['600x600'].url
