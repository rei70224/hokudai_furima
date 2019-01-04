from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MatchingOffer, MatchingOfferTalk
from hokudai_furima.core.decorators import site_rules_confirm_required
from .forms import MatchingOfferTalkForm
from django.utils import timezone
from django.conf import settings
from django.http import JsonResponse
from django.utils import html
from hokudai_furima.notification.models import Notification
from django.urls import reverse


def matching_offer_details(request, pk):
    matching_offer = get_object_or_404(MatchingOffer, pk=pk)
    talks = MatchingOfferTalk.objects.filter(matching_offer=matching_offer)
    talk_form = MatchingOfferTalkForm()
    return render(request, 'matching_offer/matching_offer_details.html', {'matching_offer': matching_offer, 'talks': talks, 'form': talk_form})


@site_rules_confirm_required
@login_required
def create_offer_talk(request):
    talker = request.user
    text = request.POST.get('text')
    matching_offer_id = request.POST.get('matching_offer_id')
    matching_offer = MatchingOffer.objects.get(id=matching_offer_id)
    created_date = timezone.now()
    talk = MatchingOfferTalk(talker=talker, matching_offer=matching_offer, text=text, created_date=created_date)
    talk.save()

    """ メール・お知らせ通知（一回でもDMにメッセージを送った人or作成者に送る）
    relative_url = reverse('matching_offer:details', kwargs={'pk': matching_offer.pk})
    joined_chat_users = matching_offer.talk_set.all().distinct('talker')
    if matching_offer.host not in joined_chat_users:
        joined_chat_users.append(matching_offer.host)
        for joined_chat_user in joined_chat_users:
            if joined_chat_user != requeset.user:
                talk_reciever = joined_chat_user
                notice = Notification(reciever=talk_reciever, message=request.user.username+'から'+matching_offer.title+'についてのDMが届いています。', relative_url=relative_url)
                notice.save()
                send_email_accept_new_message_of_matching_offer(talk_reciever.email, matching_offer, request.user.username)
    """

    d = {
        'talker': html.escape(talker.username),
        'text': html.escape(text),
        'created_date': timezone.template_localtime(created_date, settings.TIME_ZONE).strftime('%Y年%-m月%-d日%-H:%M'),
        'talk_id': talk.id,
    }
    return JsonResponse(d)


@site_rules_confirm_required
@login_required
def delete_offer_talk(request):
    talk_id = request.POST.get('talk_id')
    talk = MatchingOfferTalk.objects.get(id=talk_id)
    if request.user == talk.talker:
        talk.delete()
        d = {
            'talk_id': talk_id
        }
        return JsonResponse(d)
    else:
        return JsonResponse({'status':'false'}, status=500)
