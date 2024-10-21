from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def matches(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'web/matches.html',
        context={
            'session': request.session.get('user'),
            'page_name': 'matches'
        }
   )

