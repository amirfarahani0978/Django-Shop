# Generated by Django 4.1.4 on 2023-10-05 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0013_wishlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="product.category",
            ),
            preserve_default=False,
        ),
    ]