from django.db import models

class Evaluation(models.Model):
    name        = models.CharField(max_length=128)
    isTemplate  = models.BooleanField(blank=True)
    created     = models.DateTimeField(auto_now_add = True)
    modified    = models.DateTimeField(auto_now = True)

class QuestionType(models.Model):
    name            = models.CharField(max_length=128)
    answerDatatype  = models.CharField(max_length=16, choices = (('integer', 'integer'), ('string', 'string'),))

class Question(models.Model):
    question              = models.CharField(max_length=128)
    order               = models.IntegerField()
    questionType          = models.ForeignKey(QuestionType)
    hasExtraTextField     = models.BooleanField(blank=True)
    extraTextFieldHeading = models.CharField(max_length = 128, blank=True)

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
