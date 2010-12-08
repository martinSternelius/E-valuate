"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from e_valuate.evaluate.models import IntegerAlternative, Question, Evaluation, QuestionType

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)
    
    #Creates integer alternatives from ints and saves them
    #Asserts that they were saved with correct values
    def testGenerateFromRange(self):
      low = 1
      high = 2
      intList1 = range(low, high+1)
      testEvaluation = Evaluation(name='Test Evaluation')
      testEvaluation.save()
      testQuestionType = QuestionType()
      testQuestionType.save()
      testQuestion = Question(question='Test Question', order=1, questionType=testQuestionType, evaluation=testEvaluation)
      testQuestion.save()
      testQuestion.generateIntegerAlternatives(low, high)
      intAltList = testQuestion.integeralternative_set.all()
      intList2 = []
      for intAlt in intAltList:
        intList2.append(intAlt.value)
        
      self.failUnlessEqual(intList1, intList2)
      
    
__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

