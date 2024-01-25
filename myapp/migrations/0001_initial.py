# Generated by Django 5.0.1 on 2024-01-24 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserType",
            fields=[
                (
                    "userTypeName",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("userTypeDesc", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("userId", models.IntegerField(primary_key=True, serialize=False)),
                ("stars", models.IntegerField()),
                ("namePlate", models.CharField(max_length=50)),
                (
                    "userTypeName",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.usertype"
                    ),
                ),
            ],
        ),
    ]
