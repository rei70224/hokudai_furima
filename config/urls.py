from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'account/', include('hokudai_furima.account.urls')),
    url(r'product/', include('hokudai_furima.product.urls')),
    url(r'search/', include('hokudai_furima.search.urls')),
    url(r'chat/', include('hokudai_furima.chat.urls')),
    url(r'todo_list/', include('hokudai_furima.todo_list.urls')),
    url(r'contact/', include('hokudai_furima.contact.urls')),
    url(r'^', include('hokudai_furima.core.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 画像への直リンクを使う場合は必要。この一行がなくても、{{user.icon.url}}で表示することは可能
