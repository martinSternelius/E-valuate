#coding: utf-8
from django.db import models
from django.forms import ModelForm
from django.forms.models import modelformset_factory

class Evaluation(models.Model):
    name        = models.CharField(max_length=128)
    isTemplate  = models.BooleanField(blank=True)
    created     = models.DateTimeField(auto_now_add = True)
    modified    = models.DateTimeField(auto_now = True)

    def getAllTemplates(self):
        return Evaluation.objects.filter(isTemplate=True)

class QuestionType(models.Model):
    name            = models.CharField(max_length=128)
    answerDatatype  = models.CharField(max_length=16, choices = (('integer', 'integer'), ('string', 'string'),))
    
    def __unicode__(self):
        return self.name

class Question(models.Model):
    question                = models.CharField('fråga', max_length=128)
    order                   = models.IntegerField()
    evaluation              = models.ForeignKey(Evaluation)
    questionType            = models.ForeignKey(QuestionType, verbose_name = 'Svarstyp')
    hasExtraTextField       = models.BooleanField('Extra fritextfält', blank=True)
    extraTextFieldHeading   = models.CharField('Rubrik till extrafält', max_length = 128, blank=True)

class Respondent(models.Model):
    answeringURL  = models.URLField(max_length=64)
    email         = models.EmailField()

class Answer(models.Model):
    int_answer    = models.IntegerField(blank=True)
    string_answer = models.CharField(max_length=128, blank=True)
    question      = models.ForeignKey(Question)
    respondent    = models.ForeignKey(Respondent)

class StringAlternative(models.Model):
    value = models.CharField(max_length=128)
    question = models.ForeignKey(Question)

class IntegerAlternative(models.Model):
    value = models.IntegerField()
    question = models.ForeignKey(Question)

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'hasExtraTextField', 'extraTextFieldHeading', 'questionType')