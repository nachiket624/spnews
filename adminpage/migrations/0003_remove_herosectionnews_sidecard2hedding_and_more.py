# Generated by Django 4.1.7 on 2023-04-01 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "adminpage",
            "0002_herosectionnews_remove_herosection_sidecard1hedding_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="herosectionnews", name="sidecard2hedding",),
        migrations.RemoveField(model_name="herosectionnews", name="sidecard2image",),
        migrations.RemoveField(model_name="herosectionnews", name="sidecard2para1",),
        migrations.RemoveField(model_name="herosectionnews", name="sidecard2para2",),
    ]
