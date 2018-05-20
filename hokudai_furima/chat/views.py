from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from hokudai_furima.product.models import Product
from .forms import TalkForm
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from hokudai_furima.chat.models import Talk, Chat
from django.db.models import Q
from django.utils import html
from django.contrib.auth.decorators import login_required
from hokudai_furima.account.models import User


@login_required
def post_talk(request):
    talker=request.user
    sentence = request.POST.get('sentence')
    product_id = request.POST.get('product_id')
    talk_reciever = User.objects.get(id=request.POST.get('talk_reciever_id'))
    product = Product.objects.get(id=product_id)
    created_date = timezone.now()
    if request.user == product.seller:
        chat = Chat.objects.get(product=product, product_seller=request.user, product_wanting_user=talk_reciever)
    else:
        chat = Chat.objects.get(product=product, product_seller=talk_reciever, product_wanting_user=request.user)
    if not chat:
        return HttpResponse('invalid request')
    talk = Talk(talker=talker, chat=chat, sentence=sentence, created_date=created_date)
    talk.save()
    chat.talk_set.add(talk)
    chat.save()
    print(chat.talk_set.all())
    print(chat.__dict__)
    print(talk.__dict__)
    print(chat)

    d = {
            'talker': html.escape(talker.username),
            'sentence': html.escape(sentence),
            'created_date': timezone.template_localtime(created_date, settings.TIME_ZONE).strftime('%Y年%-m月%-d日%-H:%M'),
            'talk_id': talk.id,
            }
    return JsonResponse(d)

@login_required
def delete_talk(request):
    talk_id = request.POST.get('talk_id')
    talk = Talk.objects.get(id=talk_id)
    if request.user == talk.talker:
        talk.delete()
        d = {
                'talk_id': talk_id
            }
        return JsonResponse(d)
    else:
        return JsonResponse({'status':'false'}, status=500)
