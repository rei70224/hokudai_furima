from django.shortcuts import render

# Create your views here.
def privacy_policy(request):
    return render(request, 'site_rules/privacy_policy.html')


def tos(request):
    return render(request, 'site_rules/tos.html')
