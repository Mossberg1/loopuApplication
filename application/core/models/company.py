from django.db import models


class Company(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True
    )
    website = models.URLField(
        null=True,
        blank=True
    )
    contact_email = models.EmailField(
        unique=True,
        null=True,
        blank=True
    )    
    industry = models.ForeignKey(
        'core.Industry',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    admin = models.OneToOneField(
        'core.Profile',
        on_delete=models.SET_NULL,
        related_name='admin_company',
        null=True,
        blank=True
    )
    managers = models.ForeignKey(
        'core.Profile',
        on_delete=models.SET_NULL,
        related_name='managed_companies',
        null=True,
        blank=True
    )
    
    
    def __str__(self) -> str:
        return self.name