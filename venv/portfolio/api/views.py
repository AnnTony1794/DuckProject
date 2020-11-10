from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from blog.models import Blog, Category, Comment
from courses.models import Course, School
from projects.models import Project
from .serializers import (
    BlogSerializer, 
    CategorySerializer, 
    CourseSerializer, 
    SchoolSerializer, 
    ProjectSerializer, 
    UserSerializer,
    CommentSerializer,
)

# Create your views here.


class UserPermissions(BasePermission):
    """It only can give you back you own user"""
    def has_permission(self, request, view):
        if view.action == 'retrieve' and request.user.is_authenticated and view.queryset.first() == request.user:
            return True
        elif view.action == 'list':
            return True
        return False

@permission_classes((UserPermissions, ))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogPermissions(BasePermission):
    """You have permission to see all the blogs
    but can't create one if you are not registrated"""
    def has_permission(self, request, view):
        if not request.user.is_authenticated and view.action in {'create', 'update', 'partial_update', 'destroy'}:
            return False
        elif view.action == 'list':
            return True
        
        return super().has_permission(request, view)

@permission_classes((BlogPermissions,))
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer



class CommentsPermissions(BasePermission):
    """Can see all the comments, create and edit your owns"""
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif not request.user.is_authenticated and view.action in {'create', 'update', 'partial_update', 'destroy'}:
            return False

@permission_classes((CommentsPermissions, ))
class CommentViweSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer



class CategoryPermissions(BasePermission):
    """Can create your own categories and delete your owns."""
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif not request.user.is_authenticated and view.action in {'create', 'update', 'partial_update', 'destroy'}:
            return False
        return super().has_permission(request, view)

@permission_classes((CategoryPermissions, ))
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CoursePermissions(BasePermission):
    """Can create, edit and delete your owns."""
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif not request.user.is_authenticated and view.action in {'create', 'update', 'partial_update', 'destroy'}:
            return False
        return super().has_permission(request, view)

@permission_classes((CoursePermissions, ))
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SchoolPermissions(BasePermission):
    """Can create, edit and delete your owns."""
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif not request.user.is_authenticated and view.action in {'create', 'update', 'partial_update', 'destroy'}:
            return False
        return super().has_permission(request, view)

@permission_classes((SchoolPermissions, ))
class ShoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ProjectPermissions(BasePermission):
    """Create, edit and eliminate your owns projects."""
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif not request.user.is_authenticated and view.action in {'create', 'update', 'partial_update', 'destroy'}:
            return False
        return super().has_permission(request, view)

@permission_classes((ProjectPermissions, ))
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


