from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from hokudai_furima.product.models import Product
from .forms import TalkForm
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from hokudai_furima.chat.models import Talk, Chat
from django.db.models import Q

def post_talk(request):
    talker=request.user
    sentence = request.POST.get('sentence')
    product_id = request.POST.get('product_id')
    print("product_id"+str(product_id))
    created_date = timezone.now()
    chats = Chat.objects.filter(Q(product_id=product_id) & (Q(product_seller=request.user) | Q(product_wanting_user=request.user)))
    if not chats.exists():
        return HttpResponse('invalid request')
    else:
        chat = chats[0]
        print(chat)
    talk = Talk(talker=talker, chat=chat, sentence=sentence, created_date=created_date)
    talk.save()
    chat.talk_set.add(talk)
    chat.save()
    print(chat.talk_set.all())
    print(chat.__dict__)
    print(talk.__dict__)
    print(chat)

    d = {
            'talker': talker.username,
            'sentence': sentence,
            'created_date': created_date,
            }
    return JsonResponse(d)
    """
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
    """
