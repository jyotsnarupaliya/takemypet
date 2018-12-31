from django.db import models

# Create your models here.
class pet(models.Model):
	name = models.CharField(max_length=500)
	age = models.IntegerField()
	owner = models.IntegerField()
	category = models.CharField(max_length=500)
	date = models.DateTimeField()
	description = models.TextField()

class owner(models.Model):
	name = models.CharField(max_length=500)
	email = models.EmailField()
	address = models.TextField()
	contact = models.IntegerField()
