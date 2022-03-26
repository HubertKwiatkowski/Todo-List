from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    tagName = models.CharField(max_length=50)
    tagColor = ColorField(default='#FF0000')

    def __str__(self):
        return self.tagName

class ListItem(models.Model):
    taskName = models.CharField(max_length=200)
    taskBigName = models.CharField(max_length=200)
    taskDone = models.BooleanField(default=False)
    taskNote = models.TextField(blank=True)
    taskStartDate = models.DateField(blank=True)
    taskStartTime = models.TimeField(blank=True)
    taskEndDate = models.DateField(blank=True)
    taskEndTime = models.TimeField(blank=True)
    taskTags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.taskName

