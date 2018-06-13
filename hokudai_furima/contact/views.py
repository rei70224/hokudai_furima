from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages

def post_contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "メッセージが送信されました")
        return redirect('contact:post_success') # redirect('アプリケーション名:メソッド名')
    return render(request, 'contact/post_contact.html', {'form': form})

def post_success(request):
    return render(request, 'contact/post_success.html')