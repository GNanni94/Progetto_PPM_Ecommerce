# Generated by Django 4.2.2 on 2023-06-09 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordine', '0003_alter_ordine_data_ordine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordine',
            name='data_ordine',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 10, 26, 52, 131652)),
        ),
    ]
