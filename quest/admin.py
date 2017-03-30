from django.contrib import admin

# Register your models here.
from quest.models import Survey, Question, Response, AnswerBase, AnswerText, AnswerRadio, AnswerSelect, \
    AnswerSelectMultiple, AnswerInteger

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(AnswerBase)
admin.site.register(AnswerText)
admin.site.register(AnswerRadio)
admin.site.register(AnswerSelect)
admin.site.register(AnswerSelectMultiple)
admin.site.register(AnswerInteger)
