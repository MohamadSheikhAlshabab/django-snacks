from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class SamerView(TemplateView):
    template_name ="samer_home.html"

class SamerAboutView(TemplateView):
    template_name ="samer_about.html"