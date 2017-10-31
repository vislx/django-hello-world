# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateField('date_published')

    def __str__(self):
        return 'QText: ' + str(self.question_text)


class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return 'CText: ' + str(self.choice_text)
