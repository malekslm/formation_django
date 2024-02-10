from django.urls import path
from .views import add_numbers, add_name,add_numbers2

urlpatterns = [
    path('add2/', add_numbers2, name='add_numbers2'),
    path('add/', add_numbers, name='add_numbers'),
    path('add_name/', add_name, name='add_name'),
]
