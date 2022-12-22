# Generated by Django 4.1.4 on 2022-12-22 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True)),
                ('time', models.DateField()),
                ('total_price', models.PositiveIntegerField()),
                ('offer_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='product.offer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
