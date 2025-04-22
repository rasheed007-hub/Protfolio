from django.urls import path
from . import views

urlpatterns = [
    path('api/submit/', views.index, name='submit-form'),
]