from django.conf.urls import url, include
from rest_framework import routers
from .views import BlogViewSet, CategoryViewSet, UserViewSet, CourseViewSet, ShoolViewSet, ProjectViewSet, CommentViweSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('blog', BlogViewSet)
router.register('category', CategoryViewSet)
router.register('certificate', CourseViewSet)
router.register('school', ShoolViewSet)
router.register('project', ProjectViewSet)
router.register('comments', CommentViweSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
]