from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class landpage_view(TemplateView):
    template_name = "Home.html"