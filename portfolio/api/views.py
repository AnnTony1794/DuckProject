from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from blog.models import Blog, Category
from courses.models import Course, School
from projects.models import Project
from .serializers import BlogSerializer, CategorySerializer, CourseSerializer, SchoolSerializer, ProjectSerializer, UserSerializer

# Create your views here.

@permission_classes((IsAuthenticated, ))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer
    allowed_methods = ('GET',)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    allowed_methods = ('GET',)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    allowed_methods = ('GET',)


class ShoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    allowed_methods = ('GET',)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    allowed_methods = ('GET',)