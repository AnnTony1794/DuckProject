from django.urls import path
from .views import CoursesView, CourseView

app_name = 'courses'

urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('<int:pk>/<slug:title>', CourseView.as_view(), name='course'),
]