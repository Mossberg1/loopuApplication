from django.db import models


class Profession(models.Model):
    name = models.CharField(
        max_length=64
    )
    industry = models.ForeignKey(
        'core.Industry',
        on_delete=models.CASCADE,
        related_name='professions'
    )
    
    
    def __str__(self) -> str:
        return self.name