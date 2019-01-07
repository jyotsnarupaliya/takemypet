from django.shortcuts import render
from .models import pet, owner
from django.template import loader	
from rest_framework import viewsets
from django.http import HttpResponse
from petstore.serializers import petSerializer

# Create your views here.
class PetViewSet(viewsets.ModelViewSet):
	queryset = pet.objects.all()
	serializer_class = petSerializer



def home(request):
	template = loader.get_template('petstore/allpets.html')
	return HttpResponse(template.render({}, request))
	
