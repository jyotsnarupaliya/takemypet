from .models import owner, pet
from rest_framework import serializers

class petSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = pet
		fields = ('name','age','owner', 'category','date','description')