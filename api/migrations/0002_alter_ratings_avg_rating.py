# Generated by Django 4.1.1 on 2022-09-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ratings",
            name="avg_rating",
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
    ]
