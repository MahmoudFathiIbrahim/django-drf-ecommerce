# Generated by Django 4.2.6 on 2023-10-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]