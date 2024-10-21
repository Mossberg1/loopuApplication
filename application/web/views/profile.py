from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def profile(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'web/profile.html',
        context={
            'session': request.session.get('user'),
            'page_name': 'profile'
        }
    )