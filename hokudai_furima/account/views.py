from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import views as django_views # in login
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from .forms import (SignupForm, LoginForm)
from django.contrib.auth.decorators import login_required

# inspired: https://github.com/mirumee/saleor/blob/eb1deda79d1f36bc8ac5979fc58fc37a758c92c2/saleor/account/views.py
# How to log a user in https://docs.djangoproject.com/en/2.0/topics/auth/default/

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request=request, username=username, password=password)
        if user:
            auth.login(request, user)
        messages.success(request, ('User has created'))
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
