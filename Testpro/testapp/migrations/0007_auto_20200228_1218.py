# Generated by Django 3.0.2 on 2020-02-28 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20200227_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqdata',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 28, 12, 18, 45, 541187)),
        ),
    ]
