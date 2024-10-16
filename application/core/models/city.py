from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=64
    )
    province = models.ForeignKey(
        'core.Province',
        on_delete=models.CASCADE,
        related_name='cities'
    )
    longitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        null=True, 
        blank=True
    )
    latitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        null=True, 
        blank=True
    )
    
    
    def __str__(self):
        return f'{self.name}, {self.province}'