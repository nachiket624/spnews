# Generated by Django 4.1.7 on 2023-03-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="edittor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("eitName", models.CharField(max_length=200)),
                ("eitPassword", models.CharField(max_length=140)),
                ("accPage", models.CharField(max_length=20)),
            ],
        ),
    ]
