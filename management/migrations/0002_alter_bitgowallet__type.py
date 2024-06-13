# Generated by Django 4.2 on 2024-05-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bitgowallet",
            name="_type",
            field=models.CharField(
                choices=[("trx", "TRON"), ("sol", "Solana"), ("polygon", "Polygon")],
                max_length=20,
            ),
        ),
    ]
