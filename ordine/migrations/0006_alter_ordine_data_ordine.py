# Generated by Django 4.1 on 2023-06-09 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordine', '0005_alter_ordine_data_ordine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordine',
            name='data_ordine',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 14, 44, 20, 91876)),
        ),
    ]