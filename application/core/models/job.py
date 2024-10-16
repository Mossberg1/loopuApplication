from django.db import models


class Job(models.Model):
    EMPLOYMENT_CHOICES = [
        ("Full-time", "Heltid"),
        ("Internship", "Praktik"),
        ("Part-time", "Deltid"),
        ("Project-based", "Projektbaserad")
    ]

    EXPERIENCE_CHOICES = [
        ("Nybörjare", "Nybörjare"),
        ("Junior", "Junior"),
        ("Erfaren", "Erfaren"),
        ("Senior", "Senior"),
        ("Expert", "Expert")
    ]

    WORK_TYPE_CHOICES = [
        ("På plats", "På plats"),
        ("Distans", "Distans")
    ]
    
    
    title = models.CharField(
        max_length=64
    )
    published = models.DateTimeField(
        auto_now_add=True
    )
    industry = models.ForeignKey(
        'core.Industry',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    profession = models.ForeignKey(
        'core.Profession',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    city = models.ForeignKey(
        'core.City',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    province = models.ForeignKey(
        'core.Province',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    company = models.ForeignKey(
        'core.Company',
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    # FIXME: BEFORE PRODUCTION AZURE FILE STORAGE
    description = models.FileField(
        upload_to='descriptions/',
        null=True,
        blank=True
    )
    employment_type = models.CharField(
        max_length=32,
        choices=EMPLOYMENT_CHOICES,
        null=True,
        blank=True
    )
    minimum_experience = models.CharField(
        max_length=32,
        choices=EXPERIENCE_CHOICES,
        null=True,
        blank=True
    )
    work_type = models.CharField(
        max_length=32,
        choices=WORK_TYPE_CHOICES,
        null=True,
        blank=True
    )
    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    skills = models.ManyToManyField(
        'core.Skill',
        related_name='jobs',
        blank=True,
    )


    def __str__(self) -> str:
        return f'{self.title}, {self.company.name}'
    