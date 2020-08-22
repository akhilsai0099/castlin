from django.urls import path
from . import views
from questions.views import answer
from questions.models import Question



urlpatterns = [
    path('my-questions', views.myQuestions , name= 'myquestions'),
    path('askquestion',views.askquestion , name='askquestion'),
    path('<int:id>/', views.answer, name= 'answer'),
    path('editQuestion/<int:id>', views.editQuestion , name= 'edit'),
    path('deleteQuestion/<int:id>', views.deleteQuestion , name= 'deleteQuestion'),
    path ('analytics' , views.analytics, name = 'analytics')
]

