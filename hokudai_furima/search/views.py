from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from hokudai_furima.product.models import Product
from .forms import SearchProductForm
from django.contrib import messages
from django.conf import settings

def search_product(request):
    if request.method == "GET":
        form = SearchProductForm(request.GET)
        query = request.GET.get("q")
        if query:
            query_words = query.split(' ')
            search_results = []
            if query_words is None:
                query_words = query
            for word in query_words:
                results_by_word = Product.objects.filter(title__icontains=word).order_by('updated_date')
                for result in results_by_word:
                    if result not in search_results:
                        search_results.append(result)
            #return redirect('product:product_details', search_results_pk=products.pk, form=form)
            return render(request, 'search/product/search_product.html', {'search_results': search_results, 'form': form})

    form = SearchProductForm()
    return render(request, 'search/product/search_product.html', {'form': form})

