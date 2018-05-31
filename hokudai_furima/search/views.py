from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from hokudai_furima.product.models import Product
from .forms import SearchProductForm
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

def search_product(request):
    if request.method == "GET":
        if request.GET.get("q"):
            form = SearchProductForm(request.GET)
            search_results = search(request)
            return render(request, 'search/product/search_product.html', {'product_list': search_results, 'form': form, 'is_searched': True})

    form = SearchProductForm()
    return render(request, 'search/product/search_product.html', {'form': form, 'is_searched': False})

def search(request):
    query_keyword_string, is_sold, price_range_pair = parse_search_request(request)
    if not query_keyword_string:
        return []
    else:
        query_words = query_keyword_string.split(' ')
        search_results = []
        if query_words is None:
            query_words = query
        for word in query_words:
            if is_sold == 'all':
                results_by_word = Product.objects.filter(title__icontains=word, price__gte=price_range_pair[0], price__lt=price_range_pair[1]).order_by('updated_date')
            elif is_sold == 'sold_out':
                results_by_word = Product.objects.filter(title__icontains=word, price__gte=price_range_pair[0], price__lt=price_range_pair[1], is_sold=True).order_by('updated_date')
            elif is_sold == 'not_sold': 
                results_by_word = Product.objects.filter(title__icontains=word, price__gte=price_range_pair[0], price__lt=price_range_pair[1], is_sold=False).order_by('updated_date')
            else:
                return HttpResponse('invalid request')
            for result in results_by_word:
                if result not in search_results:
                    search_results.append(result)
        return search_results

def parse_search_request(request):
    query_keyword_string = request.GET.get("q")
    is_sold = request.GET.get("is_sold")
    if request.GET.get("price_range"):
        price_range_pair = [float(x) for x in request.GET.get("price_range").split('_')]
    else:
        price_range_pair = None
    return (query_keyword_string, is_sold, price_range_pair)
