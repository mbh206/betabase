from django.urls import path
from .views import ProjectListView, ProjectDetailView, TaskListForProjectView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:project_id>/tasks/', TaskListForProjectView.as_view(), name='project-tasks'),
]
