# Generated by Django 4.1.4 on 2022-12-23 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('restored_at', models.DateTimeField(blank=True, editable=False, help_text='This is Restored Datetime', null=True, verbose_name='Restored Datetime')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, editable=False, help_text='This is active status', verbose_name='Active status')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Catagories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('restored_at', models.DateTimeField(blank=True, editable=False, help_text='This is Restored Datetime', null=True, verbose_name='Restored Datetime')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, editable=False, help_text='This is active status', verbose_name='Active status')),
                ('expire_time', models.DateField()),
                ('start_time', models.DateField()),
                ('min_price', models.PositiveIntegerField()),
                ('max_price', models.PositiveIntegerField()),
                ('percent', models.PositiveIntegerField()),
                ('offer_code', models.CharField(max_length=100, null=True)),
                ('is_available', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('restored_at', models.DateTimeField(blank=True, editable=False, help_text='This is Restored Datetime', null=True, verbose_name='Restored Datetime')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, editable=False, help_text='This is active status', verbose_name='Active status')),
                ('amount', models.PositiveIntegerField()),
                ('descript', models.CharField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('restored_at', models.DateTimeField(blank=True, editable=False, help_text='This is Restored Datetime', null=True, verbose_name='Restored Datetime')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, editable=False, help_text='This is active status', verbose_name='Active status')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='product/%Y/%m/%d/')),
                ('price', models.PositiveIntegerField()),
                ('count_buying', models.PositiveIntegerField()),
                ('status_available', models.BooleanField()),
                ('quantity', models.PositiveIntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
                ('product_feature', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productfeature')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('restored_at', models.DateTimeField(blank=True, editable=False, help_text='This is Restored Datetime', null=True, verbose_name='Restored Datetime')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, editable=False, help_text='This is active status', verbose_name='Active status')),
                ('comment', models.CharField(max_length=200)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
