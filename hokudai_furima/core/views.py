from django.shortcuts import render
from hokudai_furima.product.models import Product
from hokudai_furima.product.utils import get_public_product_list, fetch_latest_sold_timeline

# Create your views here.
def home(request):
    latest_products = get_public_product_list(Product.objects.all().order_by('-created_date')[:16])
    latest_sold_products = fetch_latest_sold_timeline()
    return render(request, 'home.html', {'product_list': latest_products, 'latest_sold_products': latest_sold_products})

