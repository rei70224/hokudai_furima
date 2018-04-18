from django.shortcuts import render
from hokudai_furima.product.models import Product

# Create your views here.
def home(request):
    latest_products = Product.objects.all().order_by('-created_date')[:16]
    #return render(request, 'home.html', {'latest_products': latest_products})
    return render(request, 'home.html', {'product_list': latest_products})

