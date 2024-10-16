from django.db import models


class Profile(models.Model):
    DRIVERS_LICENSE_CHOICES = [
        ('B-Körort', 'B-Körort'),
        ('C-Körort', 'C-Körort'),
    ]

    LANGUAGES_CHOICES = [
        ('Svenska', 'Svenska'),
        ('Engelska', 'Engelska'),
    ]
    
    auth0_id = models.CharField(
        max_length=255, 
        unique=True
    )
    province = models.ForeignKey(
        'core.Province',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profiles'
    )
    city = models.ForeignKey(
        'core.City',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profiles'
    )
    # FIXME: BEFORE PRODUCTION AZURE FILE STORAGE
    profile_picture = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )
    # FIXME: BEFORE PRODUCTION AZURE FILE STORAGE
    description = models.FileField(
        upload_to='descriptions/',
        blank=True,
        null=True
    )
    skills = models.ManyToManyField(
        'core.Skill',
        related_name='profiles',
        blank=True,
    )
    personal_qualities = models.ManyToManyField(
        'core.PersonalQuality',
        related_name='profiles',
        blank=True,
    )
    spoken_languages = models.ManyToManyField(
        'core.Language',
        related_name='profiles',
        blank=True,
    )
    industries = models.ManyToManyField(
        'core.Industry',
        related_name='profiles',
        blank=True,
    )
    professions = models.ManyToManyField(
        'core.Profession',
        related_name='profiles',
        blank=True,
    )
    driver_license = models.CharField(
        max_length=32,
        choices=DRIVERS_LICENSE_CHOICES
    )
    
    
    def __str__(self) -> str:
        return self.auth0_id