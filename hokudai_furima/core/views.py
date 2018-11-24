from django.shortcuts import render
from hokudai_furima.product.models import Product
from hokudai_furima.product.utils import get_public_product_list, fetch_latest_sold_timeline

# Create your views here.
def home(request):
    MAX_NUM_LATEST_PRODUCT = 80
    latest_products = get_public_product_list(Product.objects.all().order_by('-created_date')[:MAX_NUM_LATEST_PRODUCT])
    latest_sold_products = fetch_latest_sold_timeline()
    return render(request, 'home.html', {'product_list': latest_products, 'latest_sold_products': latest_sold_products})

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
