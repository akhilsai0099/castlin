from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from .forms import QuestionForm
import matplotlib
matplotlib.use ('Agg')
import matplotlib.pyplot as plt
import io
import urllib
import base64


# Create your views here.

#for asking the question

def askquestion(request):
    # from forms.py
    form = QuestionForm()

    if request.method =='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            #saving a variable instance for the form
            instance = form.save(commit= False)
            #for assigning the question to the particular user
            instance.posted_by = request.user

            instance.save()


            return redirect('/')
    else:
        context = {'form': form}
        #for going to the question page 
        return render(request, 'askquestion.html',context)

#for displaying the question details and answering the question
def answer(request, id):
    if request.method == 'POST':
        desc = request.POST.get('desc')
        posted_by = request.user
        
        qid = Question.objects.get(pk=id)
        a = Answer(answer_text= desc , posted_by = posted_by , qid = qid)
        a.save()
           #f strings for keeping a variable in the the form of string
        return redirect( f'/questions/{id}/' )

    else:
        current_user = request.user
        posts = Question.objects.all()         
        num_answers = Answer.objects.filter(posted_by = current_user).count()

        question = Question.objects.get(pk=id)
        answers = Answer.objects.filter(qid_id=id).order_by('posted_by')
        context = { 'posts' : posts, 'question' : question, 'current_user' : current_user, 'answers' : answers , 'num_answers' : num_answers }
   
        return render(request, 'question.html' , context)

#for displaying the user asked questions
def myQuestions(request):
    current_user = request.user
    posts = Question.objects.filter(posted_by_id = current_user.id).order_by('-date_posted')
    questions_exist = len(posts) > 0

    context = {'current_user' : current_user, 'posts':posts,'questions_exist': questions_exist, }


    return render(request,'my_questions.html',context)

#for editing the questions
def editQuestion(request,id):

    question = Question.objects.get(pk=id)
    form = QuestionForm(instance = question)

    if request.method =='POST':
        form = QuestionForm(request.POST, instance= question)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' : form}
    return render(request,'edit-question.html' , context)

#for deleting the view

def deleteQuestion(request , id):
    question = Question.objects.get(pk=id)
    if request.method == 'POST':
        question.delete()
        return redirect('/questions/my-questions')


    context = {'question' : question} 
    return render (request, 'delete.html', context)


    
def analytics(request):
    current_user = request.user
    num_questions = Question.objects.filter(posted_by= current_user).count()
    num_answers = Answer.objects.filter(posted_by = current_user).count()
    posts = Question.objects.filter(posted_by_id = current_user.id)
    questions_exist = len(posts) > 0
    slices = [num_questions,num_answers]
    labels = ['Questions asked' , 'Questions answered']
    cols = ['cyan' , '#fcd703']
    fig, ax1 = plt.subplots(figsize = (24,10))
    ax1.pie(slices,
            colors=cols,
            startangle=180,
            shadow=True,
            explode=(0, 0),
            autopct='%1.1f%%',
            labeldistance= 0.2, 
            frame=False, 
            textprops={'fontsize': 22},)
    plt.title(f'{current_user}\'s analytics',fontsize = 40)
    ax1.legend(labels, loc = 'upper right',fontsize = 18) 
    plt.tight_layout()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png',transparent=True)
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,'analytics.html',{'data': uri ,'questions_exist': questions_exist})