from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import NewProductForm, UpdateProductForm
from django.contrib import messages
from django.conf import settings
from hokudai_furima.chat.models import Talk, Chat
from hokudai_furima.chat.forms import TalkForm
# Create your views here.
from django.http import HttpResponse
from functools import reduce
import os
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from hokudai_furima.account.models import User, Notification
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def product_list(request):
    products = product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'product/product_list.html', {'products': products})

def create_product(request):
    print("creating...")
    if request.method == "POST":
        print("form is posted")
        form = NewProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print("saving...")
            product = form.save(commit=False)
            product.seller = request.user
            product.published_date = timezone.now()
            product.save()
            print("saved")
            messages.success(request, '出品に成功しました')
            return redirect('product:product_details', pk=product.pk)
        else:
            """
            if request.user.is_authenticated:
                form = NewProductForm()
                return render(request, 'product/create_product.html', {'form': form})
            else:
                # renderだとフォームが描画されない
                #return render(request, 'main/login.html')
                return redirect(settings.LOGIN_URL)
            """
            pass

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
            product_seller_id = product.seller.id
            if product_seller_id == request.user.id:
                form = UpdateProductForm(instance=product)
                return render(request, 'product/update_product.html', {'form': form})
            # renderだとフォームが描画されない
            #return render(request, 'main/login.html')
        return redirect(settings.LOGIN_URL)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(product.wanting_users)
    talk_form = TalkForm()
    #return render(request, 'product/product_details.html', {'product': product})
    talk_records = Chat.objects.filter(product=product)
    if talk_records.exists():
        print("talk_record: "+str(talk_records))
        print(list(map(lambda x: x.talk_set.all(),list(talk_records))))
        #talk_objects = list(map(lambda x: x.talk_set.all(),list(talk_records)))
        #print(list(map(lambda x: x.sentence,list(talk_objects[0]))))
        talks = list(map(lambda x: x.talk_set.all(),list(talk_records)))[0]
    else:
        talks = []
    
    wanting_users = product.wanting_users.all()
    print("wanting")
    print(wanting_users)

        #print("talk_record: "+str(''.join(reduce(lambda x,y: x['talk']+y['talk'],list(talk_records)))))
    if request.user.is_authenticated:
        return render(request, 'product/product_details.html', {'product': product, 'form': talk_form, 'talks':talks, 'wanting_users': wanting_users})
    else:
        return render(request, 'product/product_details.html', {'product': product, 'talks':talks})

#def is_same_user(product_seller_id, login_user):
#    return login_user.id  == product_seller_id

@login_required
def want_product(request, pk):
    if request.method == 'POST':
        wanting_user = request.user
        product = get_object_or_404(Product, pk=pk)
        product.wanting_users.add(wanting_user)
        product.save()
        relative_url = reverse('product:product_details', kwargs={'pk': product.pk})
        notification = Notification(reciever=product.seller, message=wanting_user.username+'さんが「'+product.title+'」の購入を希望しました。', relative_url=relative_url)
        notification.save()
        messages.success(request, '購入希望が送信されました')
        return redirect('product:want_product_done', pk=product.pk)
    else:
        return HttpResponse('can\'t accept GET request')



def want_product_done(request, pk):
    product = get_object_or_404(Product, pk=pk)
    wanting_products = Product.objects.filter(wanting_users=request.user)
    return render(request, 'product/want_product_done.html', {'product': product, 'product_list': wanting_products})


@login_required
def cancel_want_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.wanting_users.remove(request.user)
    print(product.__dict__)
    return redirect('product:product_details', pk=product.pk)   


@login_required
def product_direct_chat(request, product_pk, wanting_user_pk):
    wanting_user = get_object_or_404(User, pk=wanting_user_pk)
    product = get_object_or_404(Product, pk=product_pk)
    if request.user == wanting_user or request.user == product.seller:
        talk_form = TalkForm()
        chat = Chat.objects.filter(product=product, product_wanting_user=wanting_user, product_seller=product.seller)
        print(chat)
        if chat.exists():
            talks = list(map(lambda x: x.talk_set.all(),list(chat)))[0]
        else:
            chat = Chat(product=product, product_wanting_user=wanting_user, product_seller=product.seller, created_date=timezone.now())
            chat.save()
            talks = []
        if request.user == product.seller:
            talk_reciever_id = wanting_user.id
        else:
            talk_reciever_id = product.seller.id 
        return render(request, 'product/product_direct_chat.html', {'product': product, 'form': talk_form, 'talks':talks, 'wanting_user': wanting_user, 'chat': chat, 'talk_reciever_id': talk_reciever_id})
    else:
        return HttpResponse('invalid request')
