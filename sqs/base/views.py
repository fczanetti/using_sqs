from django.shortcuts import render
from django.http import HttpResponse

from sqs.base import tasks


def register(request):

    tasks.somar.delay()

    return HttpResponse("Task executada")
