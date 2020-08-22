from django.forms import ModelForm
from django import forms
from .models import Question



class QuestionForm(ModelForm):
    class Meta:
        #taking the model from the models.py
        model = Question
        #Creating a array of required stuff frm models.py
        fields = ['question_title' , 'question_text']
        #for styling the required forms using a dictionary format
        widgets = {
            'question_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Your title',
                'size':'40', 
            }),
            'question_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Enter your Question's Description",
                'rows': 5,
            }),
        }