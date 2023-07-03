"""
URL configuration for it_bell_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers

from posts.views import PostViewSet
from users.view import UserViewSet


users_router = routers.DefaultRouter()
users_router.register(r'users', UserViewSet)

posts_router = routers.DefaultRouter()
posts_router.register(r'posts', PostViewSet, basename='post')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users_router.urls)),
    path('api/', include(posts_router.urls)),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
