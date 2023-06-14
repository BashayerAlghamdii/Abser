from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import path
from .models import profile
import os

class UpdateProfile(TemplateView):
    def post(self, request, **kwargs):
        user = User.objects.get(id=request.POST['id'])
        userprofile = profile.objects.get(user=user)
        userprofile.blindness_type = request.POST['blindness_type']
        userprofile.username = request.POST['username']
        userprofile.mobile_num = request.POST['mobile_num']
        user.email = request.POST['email']
        userprofile.save_base()
        user.save_base()
        return redirect('/')

class SignupView(TemplateView):
    def get_success_url(self):
        return reverse('landpage:home')
    def post(self, request, *args, **kwargs):
        data = request.POST
        user = User.objects.create_user(username=data['name'],password=data['password'],email = data['email'])
        user.is_staff = True
        profile(
            user = user,
            mobile_num = data['mobile'],
            blindness_type = data['select'] # blindness
        ).save()
        if 'next' in request.POST:
            return redirect(request.POST['next'])
        else:
            return redirect('accounts:login')

urlpatterns = [
    path("login", LoginView.as_view(template_name="Sign-in.html"), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path("sign-up", SignupView.as_view(template_name="sign-up.html"), name='sign-up'),
    path("profile", login_required(TemplateView.as_view(template_name="profile.html")), name='profile'),
    path("update", login_required(UpdateProfile.as_view()), name="update")
]
