from django.db import models
from accounts.models import profile


class contant_us(models.Model):
    content = models.TextField(default="", null=False, blank=False)
    user = models.ForeignKey(profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.username}-{self.user.id}"