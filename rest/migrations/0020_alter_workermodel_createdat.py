# Generated by Django 5.0 on 2024-05-12 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0019_alter_workermodel_createdat_alter_workermodel_entrec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workermodel',
            name='createdat',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 12, 11, 41, 33, 864264), null=True),
        ),
    ]
