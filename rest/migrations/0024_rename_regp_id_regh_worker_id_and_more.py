# Generated by Django 5.0 on 2024-05-23 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0023_alter_workermodel_createdat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regh',
            old_name='regp_id',
            new_name='worker_id',
        ),
        migrations.AlterField(
            model_name='workermodel',
            name='createdat',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 23, 11, 35, 3, 891235), null=True),
        ),
    ]
