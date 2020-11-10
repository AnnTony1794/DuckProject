from django.shortcuts import render
from django.views.generic import ListView
from .models import Pages
# Create your views here.


class CoverPageView(ListView):
    model = Pages
    template_name = 'core/cover-page.html'


class ContactView(ListView):
    model = Pages
    template_name = 'core/contact.html'


class AboutView(ListView):
    model = Pages
    template_name = 'core/about-me.html'