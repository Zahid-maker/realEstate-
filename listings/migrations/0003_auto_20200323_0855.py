# Generated by Django 3.0.4 on 2020-03-23 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200323_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 23, 8, 55, 21, 390196)),
        ),
    ]