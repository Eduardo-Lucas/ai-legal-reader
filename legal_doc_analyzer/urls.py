"""
URL configuration for legal_doc_analyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/analyzer/', include('analyzer.urls')),  # Include URLs from the analyzer app
    path('', include('core.urls', namespace='core')),  # Include URLs from the core app 
    path('/users/', include('users.urls')),  # Include URLs from the users app
    path('i18n/', include('django.conf.urls.i18n')),  # Internationalization URLs
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('analyzer/', include('analyzer.urls')),  # Include URLs from the analyzer app
    path('', include('core.urls', namespace='core')),  # Include URLs from the core app 
    path('users/', include('users.urls')),  # Include URLs from the users app
    prefix_default_language=True,  # Do not prefix with default language
)
