# Generated by Django 4.0.3 on 2022-03-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_remove_listitem_tasktag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='taskTags',
            field=models.ManyToManyField(blank=True, to='todolist.tag'),
        ),
    ]
