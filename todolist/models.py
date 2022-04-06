from django.db import models
from colorfield.fields import ColorField
from .widget import *


# class User(models.Model):
#     user_name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.user_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_color = ColorField(default='#FF0000')

    def __str__(self):
        return self.tag_name


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class ListItem(models.Model):
    task_name = models.CharField(max_length=200)
    task_status = models.ForeignKey(
        'Status', 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE
    )
    task_done = models.BooleanField(default=False)
    task_note = models.TextField(blank=True)
    task_start_date = models.DateField(blank=True)
    task_start_time = models.TimeField(blank=True)
    task_end_date = models.DateField(blank=True)
    task_end_time = models.TimeField(blank=True)
    task_tags = models.ForeignKey(
        'Tag', 
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.task_name