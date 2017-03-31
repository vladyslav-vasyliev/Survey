import json

from django.db import models


class Survey(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    QUESTOIN_TYPE = (
        ('TQ', 'Text Question'),
        ('RQ', 'Radio Question'),
        ('CQ', 'Check Question'),
        ('LQ', 'List Question'),
        ('NQ', 'Numeric Question'),
    )
    text = models.TextField()
    required = models.BooleanField()
    type = models.CharField(max_length=2, choices=QUESTOIN_TYPE)
    choices = models.TextField(blank=True, null=True,
                               help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .')

    def get_choices(self):
        return self.choices.split(',')

    def get_stat(self): # TODO
        if self.type == 'TQ':
            return {}
        elif self.type == 'RQ':
            map = {}
            for resp in self.answerbase_set.all():
                answer = resp.answerradio.body
                if answer in map:
                    map[answer] += 1
                else:
                    map[answer] = 1
            return json.dumps(map)
        elif self.type == 'CQ':
            map = {}
            for resp in self.answerbase_set.all():
                answer = resp.answerselectmultiple.body
                if answer in map:
                    map[answer] += 1
                else:
                    map[answer] = 1
            res = json.dumps(map)
            return res
        elif self.type == 'LQ':
            map = {}
            for resp in self.answerbase_set.all():
                answer = resp.answerselect.body
                if answer in map:
                    map[answer] += 1
                else:
                    map[answer] = 1
            return json.dumps(map)
        elif self.type == 'NQ':
            avg = 0
            count = 0
            for resp in self.answerbase_set.all():
                avg += resp.answerinteger.body
                count += 1
            if count > 0:
                res = avg / count
            else:
                res = 0
            return {'avg': str(round(res, 2)), 'count': count}
        return {}

    def __str__(self):
        return self.survey.name + ': ' + self.text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Response(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.survey.name + str(self.created)

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'


class AnswerBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class AnswerText(AnswerBase):
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.body


class AnswerRadio(AnswerBase):
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.body


class AnswerSelect(AnswerBase):
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.body


class AnswerSelectMultiple(AnswerBase):
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.body


class AnswerInteger(AnswerBase):
    body = models.IntegerField(blank=True, null=True)
    limit_lower = models.IntegerField(blank=True, null=True)
    limit_upper = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.body)
