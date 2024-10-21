from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse


def inbox(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'web/inbox.html',
        context={
            'session': request.session.get('user'),
            'page_name': 'inbox'
        }
    )
