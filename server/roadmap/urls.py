from django.urls import path, include
from .views import *

urlpatterns = [
    path('', sort_locations_view, name='sorted_locations'),
    # path('user_preferences/', )
]



# path('', sort_locations_view, name='sorted_locations'),
# path('user_preferences/',name = 'register_user_preferences')