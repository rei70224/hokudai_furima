# inspired: https://github.com/mirumee/saleor/blob/eb1deda79d1f36bc8ac5979fc58fc37a758c92c2/saleor/account/forms.py
# inspired:  

from django import forms
from ..account.models import User
from django.contrib.auth import forms as django_forms, update_session_auth_hash
#from django.utils.translation import pgettext, pgettext_lazy
 
class SignupForm(django_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email',)
"""
class SignupForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput)
    email = forms.EmailField(
        error_messages={
            'unique': 
                'Registration error\nThis email has already been registered.'})

    password2 = forms.CharField(max_length=50,widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password','password2')
"""

"""
labels = {
    'username': 'username',
    'email': 'Email',
    'password':  'Password',
    'password2': 'Password（確認）'
    }
"""

"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update(
                {'autofocus': ''})
    password2 = forms.CharField(max_length=50,widget=forms.PasswordInput())

    class Meta:
        model = User
        widgets = {
                'password': forms.PasswordInput(),
                }

        fields = (
            "username", "email", "password","password2"
        )
 
"""
"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザ名'
 
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
 
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
 
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（確認）'
"""
        

class LoginForm(django_forms.AuthenticationForm):
    #username = forms.CharField(
        #label='username', max_length=75)
    #username = forms.EmailField(
        #label='email', max_length=75)

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        if request:
            email = request.GET.get('email')
            print(email)
            if email:
                self.fields['username'].initial = email

