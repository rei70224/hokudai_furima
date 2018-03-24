from django.conf.urls import url, include

urlpatterns = [
    url(r'account/', include('hokudai_furima.account.urls')),
    url(r'product/', include('hokudai_furima.product.urls')),
    url(r'search/', include('hokudai_furima.search.urls')),
    url(r'chat/', include('hokudai_furima.chat.urls')),
    url(r'^', include('hokudai_furima.core.urls')),
]
