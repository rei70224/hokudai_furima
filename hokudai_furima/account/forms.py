from django import forms
from ..account.models import User
 
class SignupForm(forms.ModelForm):
 
    password2 = forms.CharField(max_length=50,widget=forms.PasswordInput())

    class Meta:
        model = User
        widgets = {
                'password': forms.PasswordInput(),
                }

        fields = (
            "username", "email", "password","password2"
        )
 
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
