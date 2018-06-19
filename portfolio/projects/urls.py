from django.urls import path
from .views import ProjectsView, ProjectView

app_name = 'projects'

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects'),
    path('<int:pk>/<slug:title>/', ProjectView.as_view(), name='project')
]
