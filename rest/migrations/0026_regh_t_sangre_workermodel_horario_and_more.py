# Generated by Django 5.0 on 2024-05-24 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0025_alter_workermodel_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='regh',
            name='t_sangre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workermodel',
            name='horario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='workermodel',
            name='createdat',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 24, 17, 58, 12, 931237), null=True),
        ),
    ]
