from django.db import models


class PersonalQuality(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )


    def __str__(self) -> str:
        return self.name