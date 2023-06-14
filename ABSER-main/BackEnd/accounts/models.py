from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField
from django.db import models


def upload_image(instance, file_name):
    img_name, ext = file_name.split(".")
    return f"profile/{instance.id}.{ext}"

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=upload_image, blank=True)
    mobile_num = PhoneField(blank=True)
    blindness_type = models.CharField(default="", max_length=35, blank=False, null=False, choices=(
        ("Protanopia (red-blind)", "Protanopia (red-blind)"),
        ("Deuteranopia (green-blind)", "Deuteranopia (green-blind)"),
        ("Tritanpoia (blue-blind)", "Tritanpoia (blue-blind)"),
        ("Monochromacy (totally colorblind)", "Monochromacy (totally colorblind)"),
    )
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.user.is_staff = True
        super().save(self, *args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='normal_user'))
