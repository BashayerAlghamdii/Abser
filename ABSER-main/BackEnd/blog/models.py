from django.db import models
from accounts.models import profile
# Create your models here.

def upload_image(instance, file_name):
    img_name ,ext = file_name.split(".")
    return f"blog/{instance.id}.{ext}"


class post(models.Model):
    title = models.CharField(default="", max_length=200, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default="", null=False, blank=False)
    image = models.ImageField(upload_to=upload_image, null=False, blank=False)
    author = models.ForeignKey(profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}-{self.author.user.username}"