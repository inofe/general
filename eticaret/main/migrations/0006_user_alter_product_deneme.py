# Generated by Django 5.1.3 on 2025-01-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_product_deneme"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("points", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="deneme",
            field=models.TextField(blank=True, null=True),
        ),
    ]
