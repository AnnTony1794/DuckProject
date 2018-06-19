from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course
# Create your views here.


class CoursesView(ListView):
    model = Course
    template_name = 'courses/courses.html'


class CourseView(DetailView):
    model = Course
    template_name = 'courses/course.html'