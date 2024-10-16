from django.db import models


class Language(models.Model):
    LANGUAGE_CHOICES = [
        ('Svenska', 'svenska'),
        ('Engelska', 'engelska'),
    ]

    name = models.CharField(
        max_length=32,
        unique=True,
        choices=LANGUAGE_CHOICES,
    )


    def __str__(self) -> str:
        return self.name