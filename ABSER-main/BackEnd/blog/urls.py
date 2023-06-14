from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import post

class postView(TemplateView):
    def get(self, request, *args, **kwargs):
        post_id = request.path.rsplit("/")[-1]
        post_detail = post.objects.get(id=post_id)
        post_img = post_detail.image
        return render(request, "post.html", {"post":post_detail})

class blogView(TemplateView):
    def get(self, request, *args, **kwargs):
        posts = post.objects.all()
        return render(request, "blog.html", {"posts":posts})

urlpatterns = [
    path("", blogView.as_view(template_name="blog.html"), name='main'),
    path("post/<int:id>", postView.as_view(template_name="post.html"), name='post'),
]