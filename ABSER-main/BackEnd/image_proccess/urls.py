from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .image_proccess import ColorBlindConverter
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .color_detector import color_detector
from .models import image as image_model
from django.shortcuts import render
from accounts.models import profile
from django.urls import path
from PIL import Image
import base64
import os


class imageConvert_views(TemplateView):
    def post(self, request, *args, **kwargs):
        img = request.FILES['img']
        print(request.POST["id"])
        user_obj = User.objects.get(id=request.POST['id'])
        user = profile.objects.get(user=user_obj)
        image_model(user=user, image=img).save()
        ext = img.name.rsplit(".")[-1]
        blindness_type = request.user.profile.blindness_type.split()[0]
        FileSystemStorage().save(f"tmp.{ext}", img)
        img_proc = ColorBlindConverter(f"tmp.{ext}")
        img_proc.convert(blindness_type)
        img_proc.writeImage()
        base64_encoded = base64.b64encode(open(f"{os.getcwd()}/tmp.{ext}", 'rb').read()).decode("utf-8")
        os.remove(f'tmp.{ext}')
        return render(request, "convert-image.html", {"img": base64_encoded,"mime_type":ext})


class colorDetector(TemplateView):
    def post(self, request, *args, **kwargs):
        img = request.FILES['img']
        user_obj = User.objects.get(id=request.POST['id'])
        user = profile.objects.get(user=user_obj)
        image_model(user=user, image=str(img.read())).save()
        ext = img.name.rsplit(".")[-1]

        FileSystemStorage().save(f"tmp.{ext}", img)

        colors = color_detector(f"{os.getcwd()}/tmp.{ext}")
        # real = ['red','blue','green','yellow']
        # colors = list(set(real).intersection(colors))
        colors = [colors[x:x+4] for x in range(0, len(colors), 4)]
        base64_encoded = base64.b64encode(open(f"{os.getcwd()}/tmp.{ext}", 'rb').read()).decode("utf-8")
        os.remove(f'tmp.{ext}')
        return render(request, "detect-color.html", {"colors": colors, "img": base64_encoded})


urlpatterns = [
    path("convert-image", login_required(imageConvert_views.as_view(
        template_name="convert-image.html")), name="convert"),
    path("detect-color", login_required(colorDetector.as_view(
        template_name="detect-color.html")), name="detect"),
    path("choice", login_required(TemplateView.as_view(
        template_name="choose.html")), name="choice")
]
