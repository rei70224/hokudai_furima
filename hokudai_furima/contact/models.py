from django.db import models

class Contact(models.Model):
    text = models.TextField(('お問い合わせ内容'), max_length=1000)
    email = models.EmailField(('メールアドレス'), default='')