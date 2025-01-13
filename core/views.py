from django.views.generic import ListView, DetailView
from .models import Project
from django.views.generic import TemplateView

class ProjectListView(ListView):
    model = Project
    template_name = 'core/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'

class HomePageView(TemplateView):
    template_name = 'core/home.html'
