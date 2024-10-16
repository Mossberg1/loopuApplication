from django.core.management.base import BaseCommand
from core.models.job import Job


class Command(BaseCommand):
    help = 'Duplicate the current jobs in the database.'

    def handle(self, *args, **kwargs):
        jobs = Job.objects.all()
        for job in jobs:
            job.pk = None
            job.save()
        self.stdout.write(self.style.SUCCESS('Jobs duplicated successfully!'))