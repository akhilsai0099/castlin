from django.contrib import admin
from .models import *
# Register your models here.


# for getting the questions and answers to admin page
admin.site.register(Question)
admin.site.register(Answer)