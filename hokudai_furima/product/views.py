from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import NewProductForm
from django.contrib import messages
from django.conf import settings

# Create your views here.
#from django import HttpResponse

def product_list(request):
    products = product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'product/product_list.html', {'products': products})

def create_product(request):
    if request.method == "POST":
        form = NewProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.published_date = timezone.now()
            product.save()
            messages.success(request, '出品に成功しました')
            return redirect('product:product_details', pk=product.pk)
    else:
        if request.user.is_authenticated is True:
            form = NewProductForm()
            return render(request, 'product/product_edit.html', {'form': form})
        else:
            # renderだとフォームが描画されない
            #return render(request, 'main/login.html')
            return redirect(settings.LOGIN_URL)



def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_details.html', {'product': product})
