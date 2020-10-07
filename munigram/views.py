# Std
from datetime import datetime
import json

# Django
from django.http import HttpResponse


def hello_world(req):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M Hrs')
    return HttpResponse('The current time is {}'.format(now))


def hi(req, name, age):
    numbers = [int(i) for i in req.GET['numbers'].split(',')]

    if age >= 18:
        data = {
            'status': 'ok',
            'numbers': sorted(numbers),
            'message': 'numbers sorted',
            'name': name
        }
    else:
        data = {
            'status': 'not ok',
            'numbers': 'unauthorized',
            'message': 'go away kid',
            'name': name
        }

    return HttpResponse(json.dumps(data, indent=4))
