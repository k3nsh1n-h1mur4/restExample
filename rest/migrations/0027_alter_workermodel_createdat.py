# Generated by Django 5.0 on 2024-05-25 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0026_regh_t_sangre_workermodel_horario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workermodel',
            name='createdat',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 25, 19, 57, 10, 531047), null=True),
        ),
    ]
