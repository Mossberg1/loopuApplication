from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def saved(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'web/saved.html',
        context={
            'session': request.session.get('user'),
            'page_name': 'saved_jobs'
        }
    )