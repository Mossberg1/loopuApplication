from django.db.models import Q, Count, Case, When, IntegerField, QuerySet
from django.core.handlers.wsgi import WSGIRequest

from core.models.job import Job


def search_database(query: str) -> QuerySet:
    results = query_database(query)
    return results


def query_database(query: str) -> QuerySet:
    """ Returns a list of combined models that match the query. """
    q = (
        Q(title__icontains=query) |
        Q(industry__name__icontains=query) |
        Q(profession__name__icontains=query) |
        Q(city__name__icontains=query) |
        Q(province__name__icontains=query) |
        Q(company__name__icontains=query) |
        Q(employment_type__icontains=query) |
        Q(minimum_experience__icontains=query) |
        Q(work_type__icontains=query) |
        Q(skills__name__icontains=query)
    )

    jobs = Job.objects.filter(q).annotate(
        relevance=Count(
            Case(
                When(title__icontains=query, then=1),
                When(industry__name__icontains=query, then=1),
                When(profession__name__icontains=query, then=1),
                When(city__name__icontains=query, then=1),
                When(province__name__icontains=query, then=1),
                When(company__name__icontains=query, then=1),
                When(employment_type__icontains=query, then=1),
                When(minimum_experience__icontains=query, then=1),
                When(work_type__icontains=query, then=1),
                When(skills__name__icontains=query, then=1),
            )
        )
    ).order_by('-relevance')

    return jobs