from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def privacy_policy(request):
    return render(request, 'site_rules/privacy_policy.html')


def tos(request):
    return render(request, 'site_rules/tos.html')


@login_required
def confirm(request):
    return render(request, 'site_rules/confirm.html')
