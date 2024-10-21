from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def blog(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        'web/blog.html',
        context={
            'session': request.session.get('user'),
            'page_name': 'blog'
        }
    )