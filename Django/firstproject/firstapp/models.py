from django.db import models

# Create your models here.
#below model will basically create a database table through migration with the database.

#thus we will begin by running "python manage.py makemigrations" and "python manage.py migrate" to effectively create 
#       the below table in the database.This action creates a new file 
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
