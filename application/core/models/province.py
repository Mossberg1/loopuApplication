from django.db import models


class Province(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )


    def __str__(self) -> str:
        return self.name
    