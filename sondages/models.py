from django.db import models


# Create your models here.
class Question(models.Model):
    question_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
