from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import views as django_views # in login
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from .forms import (SignupForm, LoginForm)
from django.contrib.auth.decorators import login_required
import uuid
from .models import Activate
from django.core.mail import send_mail

# inspired: https://github.com/mirumee/saleor/blob/eb1deda79d1f36bc8ac5979fc58fc37a758c92c2/saleor/account/views.py
# How to log a user in https://docs.djangoproject.com/en/2.0/topics/auth/default/

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # activateモデルの作成と保存。userモデルを紐づけています。
        activate_key = create_key()  # uuidを使ったランダムな文字列作成
        activate_instance = Activate(user=user, key=activate_key)
        activate_instance.save()
 
        # メール本文の「本登録はこちら！ http://...」のURLを作成する
        base_url = "/".join(request.build_absolute_uri().split("/")[:4])
        base_url_without_port = re.sub(':\d+','',base_url) 
        activation_url = "{0}/activation/{1}".format(base_url_without_port, activate_key)
 
        send_activation_mail(user.email, activation_url)

        messages.success(request, ('仮登録が完了しました。ログインするためには、認証メールのリンクにアクセスする必要があります。'))
        redirect_url = request.POST.get('next', settings.LOGIN_REDIRECT_URL)
        return redirect(redirect_url)
    ctx = {'form': form}
    return render(request, 'account/signup.html', ctx)

def login(request):
    kwargs = {
        'template_name': 'account/login.html',
        'authentication_form': LoginForm}
    return django_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def details(request):
    return render(request, 'account/details.html')

@login_required
def logout(request):
    auth.logout(request)
    #messages.success(request, ('ログアウトしました'))
    return redirect(settings.LOGIN_REDIRECT_URL)


def activation(request, key):
    """ /activation/:アクティベーションキー でアクセス。本登録画面 """
 
    # keyを使ってactivateモデルを取得
    activate = get_object_or_404(Activate, key=key)
 
    # activateモデルに紐づいたユーザオブジェクトを取得
    user = activate.user
 
    # is_activeをTrue(アカウントの有効化)にし、保存
    user.is_active = True
    user.save()
    auth.login(request, user)
 
    return render(request, 'account/details.html')

 
def create_key():
    """ ランダムな文字列を生成する """
 
    key = uuid.uuid4().hex
    return key

def send_activation_mail(to_email, activation_url):
    send_mail('仮登録が完了しました（北大フリマ）',
              "本登録は以下のURLから！\\n" + activation_url,
              settings.DEFAULT_FROM_EMAIL,
              [to_email], fail_silently=False)
