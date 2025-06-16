
#This file will be populating the 'Reservation' table in the database

#This similar to creating models in the 'Django\firstproject\firstapp\models.py' but instead of inheriting from the models class,
#               as seen in models.py line 1
#               it inherits from the 'forms' class line 1


from django import forms

#below, we import the 'model' we are going to use
from .models import Reservation

#Define theform as seen below
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
