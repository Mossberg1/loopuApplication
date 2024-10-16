from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from core.models import Job


def details(request: WSGIRequest, job_id: int) -> HttpResponse:
    if request.method == 'GET':
        job = get_object_or_404(Job, pk=job_id)
        return render(
            request,
            'web/details.html',
            context = {
                'session': request.session.get('user'),
                'page_name': 'workplaces',
                'job': job
            }
        )

