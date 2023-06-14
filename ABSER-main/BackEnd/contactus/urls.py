from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from accounts.models import profile
from .models import contant_us
from django.urls import path

# 'name': ['fahd alharib'], 'emailaddress': ['fahadalwasidi@gmail.co'], 'textarea': ['']
class feedbackView(TemplateView):
    def post(self,request, *args, **kwargs):
        data = request.POST
        content = data['content'].replace("+",' ')
        print(request.POST["id"])

        user_obj = User.objects.get(id=data['id'])
        print(user_obj)
        user = profile.objects.get(user=user_obj)
        contant_us(user=user, content=content).save()
        return redirect("landpage:home")

urlpatterns = [
    path("", login_required(TemplateView.as_view(template_name="Evaluate-the-service.html")), name='main'),
    path("form", login_required(TemplateView.as_view(template_name="evaluate-contact2.html")), name='form'),
    path("save", login_required(feedbackView.as_view()), name="feedback")
]