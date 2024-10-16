from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from core.models.job import Job


def workplaces(request: WSGIRequest) -> HttpResponse:
    job_set = None
    sections = list()

    if request.method == 'GET':
        paginator = Paginator(Job.objects.all(), 24)
        page = request.GET.get('page', 1)
        job_set = paginator.get_page(page)

        jobs = list(job_set)
        section_size = 6

        for i in range(0, len(jobs), section_size):
            sections.append(jobs[i:i + section_size])

    return render(
        request,
        'web/workplaces.html',
        context={
            'session': request.session.get('user'),
            'page_name': 'workplaces',
            'job_set': job_set,
            'first_section': sections[0],
            'second_section': sections[1],
            'third_section': sections[2],
            'fourth_section': sections[3],
        }
    )
