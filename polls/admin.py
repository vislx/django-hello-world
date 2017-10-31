# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from django.contrib import admin
from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3


# class ChoiceAdmin(admin.ModelAdmin):
#     fields = ['question', 'choice_text']


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

# Register your models here.
admin.site.register(models.Question, QuestionAdmin)
# admin.site.register(models.Choice, ChoiceAdmin)
