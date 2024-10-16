from django.db import models


class AppliedJob(models.Model):
    job = models.ForeignKey(
        'core.Job',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    applicant = models.ForeignKey(
        'core.Profile',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    applied = models.DateTimeField(
        auto_now_add=True
    )
    accepted = models.BooleanField(
        default=False
    )
    rejected = models.BooleanField(
        default=False
    )
    
    
    def __str__(self) -> str:
        return f'{self.job} - {self.applicant}'