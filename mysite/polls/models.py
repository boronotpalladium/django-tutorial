from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
        

"""
    Pasos para aplicar cambios en los models:
    python manage.py makemigrations (nombre de la app, o no)
    python manage.py migrate
"""

"""
    https://docs.djangoproject.com/es/2.1/intro/tutorial02/
"""

