from django.contrib import admin

# Register your models here.

#importing the model
from .models import Reservation

admin.site.register(Reservation)
