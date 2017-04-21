from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)

class News(models.Model):
	newsTitle=models.CharField(max_length=25)
	newsArticle=models.CharField(max_length=128)

class Fruit(models.Model):
	fruitName=models.CharField(max_length=20)
	fruitPrice=models.CharField(max_length=8)
