# Generated by Django 4.2 on 2023-06-08 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ordine", "0002_alter_ordine_data_ordine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordine",
            name="data_ordine",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 8, 23, 26, 12, 230857)
            ),
        ),
    ]