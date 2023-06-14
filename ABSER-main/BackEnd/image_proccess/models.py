from django.db import models
from accounts.models import profile


def upload_image(instance, file_name):
    ext = file_name.rsplit(".")[-1]
    return f"{instance.user.id}-{instance.id}.{ext}"

# Create your models here.


class image(models.Model):
    title = models.CharField(default="", blank=True, null=True, max_length=20)
    image = models.ImageField(upload_to=upload_image, null=False, blank=False)
    user = models.ForeignKey(profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = f"{self.user.user.username}-{self.id}"
        super().save(*args, **kwargs)
