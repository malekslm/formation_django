from django.urls import path
from .views import v_add_numbers, v_add_numbers2

urlpatterns = [
    
    path('add2/', v_add_numbers2, name='n_add_numbers2'),

    path('add/', v_add_numbers, name='n_add_numbers'),

]
