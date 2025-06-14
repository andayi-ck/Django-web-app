# Would be using a function called 'path' and 'views' thus importing them as seen
#    below
from django.urls import path
from . import views


#Define a list that contains the different addresses and their associated views.
#This list is going to be called 'urlpatterns' where we will pass in the 'path' function, with the arguements
urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloEthiopia.as_view()),
]
