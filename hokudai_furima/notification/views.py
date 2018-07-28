from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from .utils import fetch_notification_list

@login_required
def index(request):
    notification_list = fetch_notification_list(request)
    return render(request, 'notification/index.html', {'notification_list': notification_list})
