from django.contrib import admin
from django.urls import path, include
from core.views import HomePageView

urlpatterns = [
    path('__reload__/', include(('django_browser_reload.urls', 'django_browser_reload'), namespace='django_browser_reload')),
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('projects/', include('core.urls')),
]
