from django.db import models

class Contact(models.Model):
    text = models.TextField(('contact'), max_length=1000)
    email = models.EmailField(('メールアドレス'), default='')