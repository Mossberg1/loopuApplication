from django.db import models


class Document(models.Model):
    profile = models.ForeignKey(
        'core.Profile',
        on_delete=models.CASCADE,
        related_name='documents'
    )
    document = models.FileField(
        upload_to='documents/',
        blank=True,
        null=True
    )


    def __str__(self) -> str:
        return f'Document owned by: {self.profile.auth0_id}'