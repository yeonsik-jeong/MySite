from encodings import search_function
from django.contrib import admin
from pyboard.models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)