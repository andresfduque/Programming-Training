"""PLatzigram Viewa"""

from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime


def hello_world(request):
    '''return a greeting.'''
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))


def sorted(request):
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    numbers = [int(i) for i in numbers]
    numbers.sort()
    sorted_numbers = {'status': 'ok',
                      'numbers': numbers,
                      'message': 'Integers sorted successfully'
                      }
    return JsonResponse(sorted_numbers, content_type='application/json')

def say_hi(request, name, age):
    '''Return a greeting'''
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram'.format(name)
    return HttpResponse(message)