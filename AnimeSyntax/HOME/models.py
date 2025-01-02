from django.db import models
from django.utils import timezone

class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='posters/', null=True, blank=True)
    is_ongoing = models.BooleanField(default=False)
    video_url = models.URLField(null=True, blank=True)  
    created_at = models.DateTimeField(default=timezone.now)
    # Другие поля...

    def __str__(self):
        return self.title

class Episode(models.Model):
    anime = models.ForeignKey(Anime, related_name='episodes_list', on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.anime.title} - Серия {self.episode_number}"
