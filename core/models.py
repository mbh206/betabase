from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    preferred_email = models.EmailField(
        max_length=254,
        blank=False
        )
    bio = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
        )

    def __str__(self):
        return f"Profile: {self.user.username}"

class Organization(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(
        User,
        related_name='organization',
        blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    TYPE_CHOICES = [
        ('web', 'Web Application'),
        ('mobile', 'Mobile Application'),
        ('desktop', 'Desktop Application'),
        ('other', 'Other'),
    ]
    STAGE_CHOICES = [
        ('idea', 'Idea'),
        ('mvp', 'MVP'),
        ('beta', 'Beta'),
        ('live', 'Live'),
        ('maintenance', 'Maintenance'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='web'
    )
    stage = models.CharField(
        max_length=20,
        choices=STAGE_CHOICES,
        default='idea'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_projects'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TechStackItem(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tech_stack'
    )
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50, blank=True)
    doc_link = models.URLField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} ({self.version}) - {self.project.name}"

class ModelDefinition(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='model_definition'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models. DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} - {self.project.name}"

class Relationship(models.Model):
    REL_TYPE_CHOICES = [
        ('one_to_one', 'One to One'),
        ('one_to_many', 'One to Many'),
        ('many_to_many', 'Many to Many'),
    ]
    from_model = models.ForeignKey(
        ModelDefinition,
        on_delete=models.CASCADE,
        related_name='relationships_from'
    )
    to_model = models.ForeignKey(
        ModelDefinition,
        on_delete=models.CASCADE,
        related_name='relationships_to'
    )
    relationship_type = models.CharField(
        max_length=20,
        choices=REL_TYPE_CHOICES,
        default='one_to_many')
    description = models.TextField(blank=True)
    def __str__(self):
        return F"{self.from_model.name} -> {self.to_model.name} ({self.relationship_type})"

class Page(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='pages'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} - {self.project.name}"

class Task(models.Model):
    STATUS_CHOICES = [
        ('blacklog', 'Backlog'),
        ('in_progress', 'In Progress'),
        ('review', 'Review'),
        ('done', 'Done'),
    ]
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
        )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
        )
    page = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
        )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='backlog'
        )
    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"
