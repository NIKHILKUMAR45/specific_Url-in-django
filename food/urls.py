from django.urls import path

from food.views import *

app_name='anything'

urlpatterns = [
    
    path('briyani/',briyani,name='briyani'),
    

]
