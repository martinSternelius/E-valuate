from django.contrib import admin
from e_valuate.evaluate.models import *

class EvaluationAdmin(admin.ModelAdmin):
  list_display = ('name', 'isTemplate')

admin.site.register(Evaluation, EvaluationAdmin)