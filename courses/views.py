from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all() #Querying all from the Course table
    serializer_class = CourseSerializer #which is the serializer created to show named fields.  



