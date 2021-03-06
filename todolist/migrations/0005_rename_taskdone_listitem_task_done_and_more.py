# Generated by Django 4.0.3 on 2022-03-27 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_status_remove_listitem_taskbigname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='taskDone',
            new_name='task_done',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskEndDate',
            new_name='task_end_date',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskEndTime',
            new_name='task_end_time',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskName',
            new_name='task_name',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskNote',
            new_name='task_note',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskStartDate',
            new_name='task_start_date',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskStartTime',
            new_name='task_start_time',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskStatus',
            new_name='task_status',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='taskTags',
            new_name='task_tags',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tagColor',
            new_name='tag_color',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tagName',
            new_name='tag_name',
        ),
    ]
