# Generated by Django 4.0.3 on 2022-04-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_remove_listitem_task_owner_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='task_trash',
            field=models.BooleanField(default=False),
        ),
    ]
