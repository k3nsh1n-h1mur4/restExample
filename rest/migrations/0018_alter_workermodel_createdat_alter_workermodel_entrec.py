# Generated by Django 5.0 on 2024-05-12 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0017_alter_workermodel_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workermodel',
            name='createdat',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 12, 11, 36, 52, 385376), null=True),
        ),
        migrations.AlterField(
            model_name='workermodel',
            name='entRec',
            field=models.CharField(choices=[('CMNO', 'CMNO'), ('HGR 45', 'HGR 45'), ('HGR 46', 'HGR 46'), ('HGR 110', 'HGR 110'), ('HGR 180', 'HGR 180'), ('HGZ 14', 'HGZ 14'), ('HGZ 89', 'HGZ 89'), ('UMF 1', 'UMF 1'), ('UMF 2', 'UMF 2'), ('UMF 34', 'UMF 34'), ('UMF 39', 'UMF 39'), ('UMF 51', 'UMF 51'), ('UMF 52', 'UMF 52'), ('UMF 53', 'UMF 53'), ('UMF 54', 'UMF 54'), ('UMF 88', 'UMF 88'), ('UMF 93', 'UMF 93'), ('UMF 171', 'UMF 171'), ('UMF 178', 'UMF 178'), ('UMF 184', 'UMF 184'), ('SUB-DEL HIDALGO', 'SUB-DEL HIDALGO'), ('SUB-DEL JUAREZ', 'SUB-DEL JUAREZ'), ('SNTSS', 'SNTSS')], max_length=100),
        ),
    ]
