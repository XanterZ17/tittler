from django.db import models

# Create your models here.

class Anime(models.Model):
    """Аниме-объект для базы аниме"""
    name = models.CharField(max_length=200)
    episodes = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    rating = models.FloatField(null=True)
    popularity = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Anime'