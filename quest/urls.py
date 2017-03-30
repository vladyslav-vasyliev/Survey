"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from quest import views

app_name = 'quest'

urlpatterns = [
    # ex: /survey/
    url(r'^$', views.surveys, name='surveys'),
    # ex: /survey/5/
    url(r'^survey/(?P<survey_id>[0-9]+)/$', views.survey, name='survey'),
    # ex: /survey/5/statistics
    url(r'^survey/(?P<survey_id>[0-9]+)/statistics/$', views.statistics, name='statistics'),
    # ex: /survey/5/statistics/raw
    url(r'^survey/(?P<survey_id>[0-9]+)/statistics/raw$', views.raw_statistics, name='raw_statistics'),
]
