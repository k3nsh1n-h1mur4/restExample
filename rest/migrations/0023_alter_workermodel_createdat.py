# Generated by Django 5.0 on 2024-05-23 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0022_alter_workermodel_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workermodel',
            name='createdat',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 23, 11, 34, 2, 908340), null=True),
        ),
    ]
