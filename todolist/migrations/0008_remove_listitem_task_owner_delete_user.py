# Generated by Django 4.0.3 on 2022-04-07 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_user_listitem_task_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='task_owner',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
