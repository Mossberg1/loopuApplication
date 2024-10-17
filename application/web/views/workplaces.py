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
            'first_section': sections[0] if len(sections) > 0 else [],
            'second_section': sections[1] if len(sections) > 1 else [],
            'third_section': sections[2] if len(sections) > 2 else [],
            'fourth_section': sections[3] if len(sections) > 3 else [],
            'last_page_minus_one': job_set.paginator.num_pages - 1,
            'last_page_minus_two': job_set.paginator.num_pages - 2
        }
    )
