

from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import TaskiSerializer

# import the Todo model from the models file
from .models import Taski

# create a class for the Todo model viewsets
class TaskiView(viewsets.ModelViewSet):

	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = TaskiSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = Taski.objects.all()
