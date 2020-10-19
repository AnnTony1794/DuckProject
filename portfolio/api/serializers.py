from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Blog, Category, Comment
from courses.models import Course, School
from projects.models import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class BlogSerializer(serializers.HyperlinkedModelSerializer):
     
     categories = serializers.StringRelatedField(many=True)

     class Meta:
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    categories = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Course
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'