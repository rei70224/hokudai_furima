from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import NewProductForm
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
        if request.user.is_authenticated is True:
            form = NewProductForm()
            return render(request, 'product/product_edit.html', {'form': form})
        else:
            # renderだとフォームが描画されない
            #return render(request, 'main/login.html')
            return redirect(settings.LOGIN_URL)



def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    talk_form = TalkForm()
    #return render(request, 'product/product_details.html', {'product': product})
    talk_records = Chat.objects.filter(product_id=product.id)
    print("talk_record: "+str(talk_records))
    print(list(map(lambda x: x.talk_set.all(),list(talk_records))))
    talk_objects = list(map(lambda x: x.talk_set.all(),list(talk_records)))
    print(list(map(lambda x: x.sentence,list(talk_objects[0]))))

    #print("talk_record: "+str(''.join(reduce(lambda x,y: x['talk']+y['talk'],list(talk_records)))))
    if request.user.is_authenticated:
        return render(request, 'product/product_details.html', {'product': product, 'form': talk_form, 'talks':list(map(lambda x: x.talk_set.all(),list(talk_records)))[0]})
    else:
        return render(request, 'product/product_details.html', {'product': product, 'talks':list(map(lambda x: x.talk_set.all(),list(talk_records)))[0]})


