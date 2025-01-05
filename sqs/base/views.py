from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sqs.base import tasks
import json


@csrf_exempt
def register(request):

    data = json.loads(request.body.decode())

    tasks.register.delay(data)

    return JsonResponse(data)
