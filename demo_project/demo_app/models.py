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

class user(models.Model):
	email=models.CharField(max_length=20)
	username=models.CharField(max_length=12)
	password=models.CharField(max_length=20)
	sex=models.CharField(max_length=2)
	age=models.CharField(max_length=4)
	hobby=models.CharField(max_length=20)
	taste=models.CharField(max_length=12)
	title=models.CharField(max_length=64)
	collect=models.CharField(max_length=12)

class tiezi(models.Model):
	title=models.CharField(max_length=32)	
	author=models.CharField(max_length=12)
	datetime=models.CharField(max_length=12)
	article=models.CharField(max_length=128)
	topic=models.CharField(max_length=4)
	zan=models.CharField(max_length=12)
	reply=models.CharField(max_length=12)
	look=models.CharField(max_length=12)

class food(models.Model):
	name=models.CharField(max_length=12)
	comment=models.CharField(max_length=4)
	comment_id=models.CharField(max_length=4)
	hotspot=models.CharField(max_length=4)
	author=models.CharField(max_length=12)
	image=models.CharField(max_length=12)
	
