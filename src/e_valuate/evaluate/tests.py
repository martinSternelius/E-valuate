#coding: utf-8
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from e_valuate.evaluate.models import IntegerAlternative, Question, Evaluation, QuestionType
from django.db.models.query import QuerySet
from django.http import HttpRequest

class SimpleTest(TestCase):
  
    def setUp(self):
      self.testEvaluation = Evaluation.objects.create(name='Test Evaluation')
      self.testQuestionTypeInt = QuestionType.objects.create(name='Flerval - Talintervall', answerDatatype='integer')
      self.testQuestionTypeString = QuestionType.objects.create(name='Flerval - Ett Svar', answerDatatype='string')
      self.testQuestionInt = Question.objects.create(question='Test Question 1', order=1, questionType=self.testQuestionTypeInt, evaluation=self.testEvaluation)
      self.testQuestionString = Question.objects.create(question='Test Question 2', order=2, questionType=self.testQuestionTypeString, evaluation=self.testEvaluation)
      self.request = HttpRequest()
      
    #Creates integer alternatives from ints and saves them
    #Asserts that they were saved with correct values
    def testGenerateIntegerAlternatives(self):
      low = 1
      high = 2
      intList1 = range(low, high+1)
      self.testQuestionInt.generateIntegerAlternatives(low, high)
      intAltList = self.testQuestionInt.integeralternative_set.all()
      intList2 = []
      for intAlt in intAltList:
        intList2.append(intAlt.value)
        
      self.failUnlessEqual(intList1, intList2)
      
    def testGenerateStringAlternatives(self):
      string = 'yes,no,maybe'
      stringList1 = string.split(',')
      self.testQuestionString.generateStringAlternatives(string)
      stringAltList = self.testQuestionString.stringalternative_set.all()
      stringList2 = []
      for stringAlt in stringAltList:
        stringList2.append(stringAlt.value)
        
      self.failUnlessEqual(stringList1, stringList2)
      
    def testGetNextOrder(self):
      nextOrder1 = self.testEvaluation.getNextQuestionOrder() #Has 2 questions, next question order should = 3
      #Evaluation without questions - next question order should = 1
      testEvaluation2 = Evaluation(name='X')
      nextOrder2 = testEvaluation2.getNextQuestionOrder()
      self.failUnlessEqual(3, nextOrder1)
      self.failUnlessEqual(1, nextOrder2)
    
__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

