# Generated by Django 4.1.7 on 2023-03-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="roomNumber",
            field=models.BigIntegerField(unique=True),
        ),
    ]
