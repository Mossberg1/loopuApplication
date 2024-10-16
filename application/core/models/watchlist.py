from django.db import models


class Watchlist(models.Model):
    job = models.ForeignKey(
        'core.Job',
        on_delete=models.CASCADE,
        related_name='watchlist'
    )
    user = models.ForeignKey(
        'core.Profile',
        on_delete=models.CASCADE,
        related_name='watchlist'
    )
    added = models.DateTimeField(
        auto_now_add=True
    )
    
    
    def __str__(self) -> str:
        return f'{self.job} - {self.user}'