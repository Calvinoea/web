# Generated by Django 2.2.4 on 2020-07-28 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0132_auto_20200728_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribessubscription',
            name='expires_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 11, 14, 15, 141105, tzinfo=utc), null=True),
        ),
    ]
