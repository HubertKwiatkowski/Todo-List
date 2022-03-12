from django.db import models


class ListItem(models.Model):
    taskName = models.CharField(max_length=200)
    taskDone = models.BooleanField()
    taskNote = models.TextField(blank=True)
    taskDeadline = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.taskName