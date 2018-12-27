from django.http import JsonResponse, HttpResponse
from django.conf import settings
import urllib.request
import json


def get_price_from_isbn_rakuten(request):
    isbn = request.GET.get('isbn', '')
    price = search_rakuten_book_api(isbn)
    if price is not None:
        return JsonResponse({'price': price})
    else:
        return HttpResponse(status=500)


def search_rakuten_book_api(isbn):
    application_id = settings.RAKUTEN_APPLICATION_ID
    print(settings)
    url = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404'
    params = {
        "applicationId": application_id,
        "isbn": isbn,
    }

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
    with urllib.request.urlopen(req) as res:
        body = res.read()
        body_json = json.loads(body)
        try:
            price = body_json['Items'][0]['Item']['itemPrice']
        except ValueError:
            price = None
        return price
