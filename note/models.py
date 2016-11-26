from django.db import models
from django.urls import reverse
from django.utils import timezone


class Note(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    created_date = models.DateTimeField(
        default=timezone.now
    )
    author = models.ForeignKey('auth.User', default=0)
    # file = models.FileField(upload_to='upload/', default='', blank=True)
    #
    # def add(self):
    #     self.created_date = timezone.now()
    #     self.save()
    #
    def __str__(self):
        return self.title