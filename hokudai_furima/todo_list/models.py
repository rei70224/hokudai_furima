from django.db import models
from django.conf import settings
from hokudai_furima.product.models import Product

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    is_done = models.BooleanField(default=False)
    message = models.TextField(max_length=256, null=True) 
    relative_url = models.TextField(max_length=256, null=True) 

    def done(self):
        self.is_done = True

class ReportToBuyTodo(Todo):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)

    def set_template_message(self, wanting_user):
        self.message='販売を決定した「'+self.product.title+'」の取引方法について、'+'購入者「'+wanting_user.username+'」とチャットで取引方法を確認し合ってください'
