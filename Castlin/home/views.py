from django.shortcuts import render
from questions.models import Question
# Create your views here.

def index(request):
    posts = Question.objects.all().order_by('-date_posted')
    return render(request, 'index.html' , {'posts' : posts})