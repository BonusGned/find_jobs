"""find_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import logout
from django.urls import path, include

from find_jobs import settings
from users.urls import router
from users.views import user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include(('social_django.urls', 'social_django.urls'), namespace='social')),
    path('logout/', user_logout, name='logout'),
    path('vacancies/', include('vacancies.urls')),
    path('', include((router.urls, 'users.urls'), namespace='users')),
]
