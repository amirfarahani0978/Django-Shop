# Generated by Django 4.1.4 on 2023-07-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_rename_banner_baner_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="baner",
            name="title",
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]