from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from authentication.forms import MessageForm
from quest.models import Survey, Response, AnswerText, AnswerRadio, AnswerSelect, AnswerSelectMultiple, AnswerInteger


def surveys(request):
    try:
        surveys = Survey.objects.all()
    except Exception as e:
        form = MessageForm(e, '/')
        return render(request, 'msg.html', {'form': form})
    context = {'title': 'Surveys', 'surveys': surveys}
    return render(request, 'surveys.html', context)


def survey(request, survey_id):
    if len(request.POST) > 0:
        return submit(request, survey_id)
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Exception as e:
        form = MessageForm(e, '/')
        return render(request, 'msg.html', {'form': form})
    context = {'title': 'Survey', 'survey': survey}
    return render(request, 'survey.html', context)


def submit(request, survey_id):
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Exception as e:
        form = MessageForm(e, '/')
        return render(request, 'msg.html', {'form': form})
    items = list(request.POST.items())

    response = Response()
    response.survey = survey
    try:
        response.save()
    except Exception as e:
        form = MessageForm(e, '/')
        return render(request, 'msg.html', {'form': form})
    for question in survey.question_set.all():
        answers = [item for item in items if ('q' + question.type + str(question.id)) in item[0]]
        for answer in answers:
            if question.type == 'TQ':  # Text Question
                res = AnswerText()
            elif question.type == 'RQ':  # Radio Question
                res = AnswerRadio()
            elif question.type == 'CQ':  # Check Question
                res = AnswerSelectMultiple()
            elif question.type == 'LQ':  # List Question
                res = AnswerSelect()
            elif question.type == 'NQ':  # Numeric Question
                res = AnswerInteger()

            if res is not None:
                res.question = question
                res.response = response
                res.body = answer[1]
                try:
                    res.save()
                except Exception as e:
                    form = MessageForm(e, '/')
                    return render(request, 'msg.html', {'form': form})
    return render(None, 'thanks.html', {})


def statistics(request, survey_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Exception as e:
        form = MessageForm(e, '/')
        return render(request, 'msg.html', {'form': form})
    context = {'title': 'Survey', 'survey': survey}
    return render(request, 'statistics.html', context)


def raw_statistics(request, survey_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Exception as e:
        form = MessageForm(e, '/')
        return render(request, 'msg.html', {'form': form})
    context = {'title': 'Survey', 'survey': survey}
    return render(request, 'raw_statistics.html', context)
