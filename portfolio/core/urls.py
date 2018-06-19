from django.urls import path
from .views import CoverPageView, ContactView, AboutView

app_name = 'core'

urlpatterns = [
    path('', CoverPageView.as_view(), name='cover-page'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-me/', AboutView.as_view(), name='about-me')
]
