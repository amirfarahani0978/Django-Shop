# Generated by Django 4.1.4 on 2023-01-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='static/images/default.png', upload_to='profile/%Y/%m/%d/'),
        ),
    ]
