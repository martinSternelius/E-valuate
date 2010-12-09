# coding:utf-8
from django import forms
from django.db import models
from django.forms import ModelForm

class Evaluation(models.Model):
  name        = models.CharField(max_length=128, verbose_name="Utvärderingens Namn")
  isTemplate  = models.BooleanField(blank=True)
  created     = models.DateTimeField(auto_now_add = True)
  modified    = models.DateTimeField(auto_now = True)
  
  def __unicode__(self):
    return self.name

  def getAllTemplates(self):
    return Evaluation.objects.filter(isTemplate=True)
  
  def getNextQuestionOrder(self):
    questions = self.question_set.all().order_by('-order')
    nextOrder = questions[0].order+1 if len(questions) > 0 else 1
    return nextOrder
  
class QuestionType(models.Model):
  name            = models.CharField(max_length=128)
  answerDatatype  = models.CharField(max_length=16, choices = (('integer', 'integer'), ('string', 'string'),))
  hasAlternatives = models.BooleanField()
  
  def __unicode__(self):
    return self.name
  
class Question(models.Model):
  question              = models.CharField('fråga', max_length=128)
  order                 = models.IntegerField()
  questionType          = models.ForeignKey(QuestionType, verbose_name = 'Svarstyp')
  evaluation            = models.ForeignKey(Evaluation)
  hasExtraTextField     = models.BooleanField('Extra fritextfält', blank=True)
  extraTextFieldHeading   = models.CharField('Rubrik till extrafält', max_length = 128, blank=True)
  
  def __unicode__(self):
    return self.question
  
  def generateIntegerAlternatives(self, low, high):
    intList = range(low, high+1)
    for int in intList:
      integerAlternative = IntegerAlternative(value=int, question=self)
      integerAlternative.save()
      
  def generateStringAlternatives(self, string):
    stringList = string.split(',')
    for string in stringList:
      stringAlternative = StringAlternative(value=string, question=self)
      stringAlternative.save()
    
class Respondent(models.Model):
  answeringURL  = models.URLField(max_length=64)
  email         = models.EmailField()
  
  def __unicode__(self):
    return self.email
  
class Answer(models.Model):
  int_answer    = models.IntegerField(blank=True)
  string_answer = models.CharField(max_length=128, blank=True)
  question      = models.ForeignKey(Question)
  respondent    = models.ForeignKey(Respondent)
  
  def __unicode__(self):
    return self.int_answer.to_s + self.string_answer

class StringAlternative(models.Model):
  question = models.ForeignKey(Question)
  value = models.CharField(max_length=128)
  question = models.ForeignKey(Question)
      
  def __unicode__(self):
    return self.value
  
class IntegerAlternative(models.Model):
  value = models.IntegerField()
  question = models.ForeignKey(Question)
  
  def __unicode__(self):
    return self.value
    
class EvaluationForm(ModelForm):
  class Meta:
    exclude = ('isTemplate', 'created', 'modified')
    model = Evaluation

class QuestionForm(ModelForm):
  class Meta:
    model = Question
    fields = ('question', 'hasExtraTextField', 'extraTextFieldHeading', 'questionType')
    
class IntegerAlternativeForm(forms.Form):
  low = forms.IntegerField('Maximum')
  high = forms.IntegerField('Minimum')
  
  def clean(self):
    cleaned_data = self.cleaned_data
    high = cleaned_data.get('high')
    low = cleaned_data.get('low')
    
    if high and low:
      if high <= low:
        raise forms.ValidationError('Talen måste skrivas från lägst till högst, och det högra talet måste vara högre än det vänstra!')
      
    return cleaned_data
  
class StringAlternativeForm(forms.Form):
  alternatives = forms.CharField('Skriv in svarsalternativ separerade med kommatecken')
