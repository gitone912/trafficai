# Generated by Django 4.2.1 on 2023-06-14 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Intersection",
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
            ],
        ),
        migrations.CreateModel(
            name="TrafficData",
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
                ("traffic_density", models.IntegerField()),
                ("vehicle_size", models.CharField(max_length=50)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "intersection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.intersection",
                    ),
                ),
            ],
        ),
    ]