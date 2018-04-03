from django.shortcuts import render
from hokudai_furima.product.models import Product

# Create your views here.
def home(request):
    #latest_products = Product.objects.order_by('created_date')[:10]
    #return render(request, 'home.html', {'latest_products': latest_products})
    return render(request, 'home.html')

