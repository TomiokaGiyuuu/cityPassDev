from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('search/', get_place_id_through_name, name='search_place'),
    path('places/<int:place_id>/', get_place_by_id, name='get_place_by_id'),
    path('chat/', conversation, name='conversation')
]