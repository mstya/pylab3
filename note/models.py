from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    author = models.ForeignKey('auth.User')

    def add(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
