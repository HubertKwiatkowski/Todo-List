# Generated by Django 4.0.3 on 2022-03-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_rename_taskdeadline_listitem_taskdeadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='taskTag',
            field=models.TextField(blank=True),
        ),
    ]
