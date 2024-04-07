from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'courses'

router = routers.DefaultRouter()
router.register('subjects', views.SubjectViewSet)
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
