from rest_framework import generics
from rest_framework import viewsets

from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer, CourseSerializer


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
