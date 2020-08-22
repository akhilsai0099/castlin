from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=50)
    question_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add= True)
    posted_by = models.ForeignKey(User , on_delete=models.CASCADE)
   # for getting question title of in admin page!
    def __str__(self):
        return self.question_title


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey(Question , on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add= True)
    posted_by = models.ForeignKey(User , on_delete=models.CASCADE)
    

