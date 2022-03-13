from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    tagName = models.CharField(max_length=50, blank=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.tagName

class ListItem(models.Model):
    taskName = models.CharField(max_length=200)
    taskDone = models.BooleanField()
    taskNote = models.TextField(blank=True)
    taskStartDate = models.DateField(auto_now=True, auto_now_add=False)
    taskDeadline = models.DateField(auto_now=False, auto_now_add=False)
    taskTags = models.ManyToManyField('Tag', blank=True)


    def __str__(self):
        return self.taskName

