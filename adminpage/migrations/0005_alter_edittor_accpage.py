# Generated by Django 4.1.7 on 2023-04-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0004_herosectionnews_newsauthor_herosectionnews_newstime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="edittor",
            name="accPage",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1", "Sport"),
                    ("2", "Education"),
                    ("3", "politics"),
                    ("4", "Nation"),
                    ("4", "State"),
                ],
                max_length=32,
                null=True,
            ),
        ),
    ]
