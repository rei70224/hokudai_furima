# inspired: https://github.com/mirumee/saleor/blob/eb1deda79d1f36bc8ac5979fc58fc37a758c92c2/saleor/account/forms.py

from django import forms
from ..account.models import User
from django.contrib.auth import forms as django_forms, update_session_auth_hash
 
class SignupForm(django_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email',)
        

class LoginForm(django_forms.AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        if request:
            email = request.GET.get('email')
            print(email)
            if email:
                self.fields['username'].initial = email

