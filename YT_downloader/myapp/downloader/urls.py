from django.urls import path
from .views import *

urlpatterns = [
    path('', youtube, name='youtube'),
]
