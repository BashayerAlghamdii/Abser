from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="Home.html"), name='home'),
    path("services", TemplateView.as_view(template_name="services.html"), name="services")
]