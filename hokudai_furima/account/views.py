from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth import views as django_views
# from
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
# from django.utils.tran
from .forms import (SignupForm)

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

