from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import views as django_views # in login
# from
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
# from django.utils.tran
from .forms import (SignupForm, LoginForm)
from django.contrib.auth.decorators import login_required

# inspired: https://github.com/mirumee/saleor/blob/eb1deda79d1f36bc8ac5979fc58fc37a758c92c2/saleor/account/views.py

def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = auth.authenticate(request=request, email=email, password=password)
        if user:
            #auth.login(request, user)
            pass
        messages.success(request, ('User has created'))
        redirect_url = request.POST.get('next', settings.LOGIN_REDIRECT_URL)
        return redirect(redirect_url)
    ctx = {'form': form}
    #return TemplateResponse(request, 'account/signup.html', ctx)
    return render(request, 'account/signup.html', ctx)

def login(request):
    kwargs = {
        'template_name': 'account/login.html',
        'authentication_form': LoginForm}
    print(request.POST)
    return django_views.LoginView.as_view(**kwargs)(request, **kwargs)


@login_required
def details(request):
    return render(request, 'account/details.html')

@login_required
def logout(request):
    auth.logout(request)
    #messages.success(request, ('ログアウトしました'))
    print(settings.LOGIN_REDIRECT_URL)
    return redirect(settings.LOGIN_REDIRECT_URL)
