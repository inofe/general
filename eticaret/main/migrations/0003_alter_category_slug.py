# Generated by Django 5.1.3 on 2025-01-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_variation_img_alter_category_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
