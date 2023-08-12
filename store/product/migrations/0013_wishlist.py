# Generated by Django 4.1.4 on 2023-08-12 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0012_alter_comment_product_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="WishList",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        editable=False,
                        help_text="This is deleted datetime",
                        null=True,
                        verbose_name="Deleted Datetime",
                    ),
                ),
                (
                    "restored_at",
                    models.DateTimeField(
                        blank=True,
                        editable=False,
                        help_text="This is Restored Datetime",
                        null=True,
                        verbose_name="Restored Datetime",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        editable=False,
                        help_text="This is deleted status",
                        verbose_name="Deleted status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        editable=False,
                        help_text="This is active status",
                        verbose_name="Active status",
                    ),
                ),
                (
                    "product",
                    models.ManyToManyField(
                        related_name="product", to="product.product"
                    ),
                ),
                (
                    "user_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]