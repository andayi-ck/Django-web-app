from django.db import models

# Create your models here.
#below model will basically create a database table through migration with the database.

#thus we will begin by running "python manage.py makemigrations" and "python manage.py migrate" to effectively create 
#       the below table in the database.This action creates a new file 
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


#below is a table 'Reservation' with 5 different columns that is going to be populated
#       using a form, created in the file Django\firstproject\firstapp\forms.py
class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)


