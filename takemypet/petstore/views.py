from django.shortcuts import render
from .models import pet, owner
from rest_framework import viewsets
from petstore.serializers import petSerializer

# Create your views here.
class PetViewSet(viewsets.ModelViewSet):
	queryset = pet.objects.all()
	serializer_class = petSerializer
	
