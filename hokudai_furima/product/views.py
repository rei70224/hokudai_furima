from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import NewProductForm, UpdateProductForm
from django.contrib import messages
from django.conf import settings
from hokudai_furima.chat.models import Talk, Chat
from hokudai_furima.chat.forms import TalkForm
# Create your views here.
#from django import HttpResponse
from functools import reduce

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
        if request.user.is_authenticated:
            form = NewProductForm()
            return render(request, 'product/create_product.html', {'form': form})
        else:
            # renderだとフォームが描画されない
            #return render(request, 'main/login.html')
            return redirect(settings.LOGIN_URL)

def update_product(request, product_pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_pk)
        form = UpdateProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.published_date = timezone.now()
            product.save()
            messages.success(request, '商品情報を更新しました')
            return redirect('product:product_details', pk=product.pk)
    else:
        if request.user.is_authenticated:
            product = get_object_or_404(Product, pk=product_pk)
            product_id = product.id
            product_seller_id = product.seller.id
            if product_seller_id == request.user.id:
                form = UpdateProductForm(instance=product)
                return render(request, 'product/update_product.html', {'form': form})
            # renderだとフォームが描画されない
            #return render(request, 'main/login.html')
        return redirect(settings.LOGIN_URL)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    talk_form = TalkForm()
    #return render(request, 'product/product_details.html', {'product': product})
    talk_records = Chat.objects.filter(product_id=product.id)
    if talk_records.exists():
        print("talk_record: "+str(talk_records))
        print(list(map(lambda x: x.talk_set.all(),list(talk_records))))
        #talk_objects = list(map(lambda x: x.talk_set.all(),list(talk_records)))
        #print(list(map(lambda x: x.sentence,list(talk_objects[0]))))
        talks = list(map(lambda x: x.talk_set.all(),list(talk_records)))[0]
    else:
        talks = []

        #print("talk_record: "+str(''.join(reduce(lambda x,y: x['talk']+y['talk'],list(talk_records)))))
    if request.user.is_authenticated:
        return render(request, 'product/product_details.html', {'product': product, 'form': talk_form, 'talks':talks})
    else:
        return render(request, 'product/product_details.html', {'product': product, 'talks':talks})

#def is_same_user(product_seller_id, login_user):
#    return login_user.id  == product_seller_id
