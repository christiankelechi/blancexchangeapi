# Generated by Django 4.2.11 on 2024-06-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0002_alter_bitgowallet__type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bitgowallet",
            name="wallet_id",
            field=models.CharField(max_length=50),
        ),
    ]
