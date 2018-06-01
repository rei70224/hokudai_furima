from django.db import models
from django.conf import settings

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    is_done = models.BooleanField(default=False)
    message = models.TextField(max_length=256, null=True) 
    relative_url = models.TextField(max_length=256, null=True) 

    def done(self):
        self.is_done = True
