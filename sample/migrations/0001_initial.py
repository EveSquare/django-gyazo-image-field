# Generated by Django 5.0.1 on 2024-01-06 02:56

import models.GyazoImageField
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SampleUserProfileModel",
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
                ("name", models.CharField(max_length=255)),
                ("age", models.PositiveIntegerField()),
                ("profile_image", models.GyazoImageField.GyazoImageField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "SampleUserProfileModel",
                "verbose_name_plural": "SampleUserProfileModels",
            },
        ),
    ]
