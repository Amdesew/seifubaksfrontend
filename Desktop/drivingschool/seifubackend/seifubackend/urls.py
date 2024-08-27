"""
URL configuration for seifubackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from seifu.views import Home, Result, NewStudentViewset, StudentResultViewset, NewStudentView #submit_form
from seifu.models import NewStudent, StudentResult
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'NewStudent', NewStudentViewset)
router.register(r'StudentResult', StudentResultViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('results/', Result),
    path('api/', include(router.urls)),
    path('api/NewStudent/', NewStudentView.as_view(), name='new_student'),
]
