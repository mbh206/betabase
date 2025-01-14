from django.contrib import admin
from .models import Project, Task, Page, ModelDefinition, Relationship, TechStackItem, Organization

admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Page)
admin.site.register(ModelDefinition)
admin.site.register(Relationship)
admin.site.register(TechStackItem)
