from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)

class News(models.Model):
	newsTitle=models.CharField(max_length=25)
	newsArticle=models.CharField(max_length=128)

class helfruit(models.Model):
	rfoodname=models.CharField(max_length=20)
	rheat=models.CharField(max_length=8)
	rfat=models.CharField(max_length=8)
	rcellulose=models.CharField(max_length=8)
	rco2=models.CharField(max_length=8)
	rprotein=models.CharField(max_length=8)
	rvia=models.CharField(max_length=8)
	raccess=models.CharField(max_length=128)
