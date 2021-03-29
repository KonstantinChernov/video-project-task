from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to=f'videos/',
                             validators=[FileExtensionValidator(['mp4', 'ogg', 'ogv', 'webm', 'mvk', 'avi'])])

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
