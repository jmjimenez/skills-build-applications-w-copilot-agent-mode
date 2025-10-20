"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from octofit_tracker import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('/users/'),
    # Use CODESPACE_NAME env variable for endpoint URLs
    'teams': _build_api_url('teams/'),
    'activities': _build_api_url('activities/'),
    'workouts': _build_api_url('workouts/'),
    'leaderboard': _build_api_url('leaderboard/'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]

# Helper function to build API URLs using CODESPACE_NAME
import os
from django.http import HttpRequest

def _build_api_url(path: str, request: HttpRequest = None) -> str:
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        return f'https://{codespace}-8000.app.github.dev/api/{path}'
    if request:
        return request.build_absolute_uri(f'/api/{path}')
    return f'http://localhost:8000/api/{path}'
