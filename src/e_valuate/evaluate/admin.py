from django.contrib import admin
from e_valuate.evaluate.models import *

class EvaluationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'isTemplate')
  
class QuestionAdmin(admin.ModelAdmin):
  list_display = ('id', 'question', 'questionType')
  
class QuestionTypeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'answerDatatype')

class StringAlternativeAdmin(admin.ModelAdmin):
  list_display = ('id', 'value', 'question')

class IntegerAlternativeAdmin(admin.ModelAdmin):
  list_display = ('id', 'value', 'question')


admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionType, QuestionTypeAdmin)
admin.site.register(StringAlternative, StringAlternativeAdmin)
admin.site.register(IntegerAlternative, IntegerAlternativeAdmin)
