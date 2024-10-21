from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def plus(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'web/plus.html',
        context={
            'session': request.session.get('user'),
            'page_name': 'loopu_plus'
        }
    )