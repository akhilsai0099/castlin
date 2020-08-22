from django.urls import path
from . import views
from questions.models import Question

urlpatterns = [
    path('', views.index , name= 'index'),
]

