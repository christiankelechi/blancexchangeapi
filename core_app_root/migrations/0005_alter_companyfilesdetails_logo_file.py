# Generated by Django 4.2.11 on 2024-06-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_app_root", "0004_alter_companyfilesdetails_logo_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyfilesdetails",
            name="logo_file",
            field=models.ImageField(
                height_field=278, max_length=1000, upload_to="", width_field=278
            ),
        ),
    ]
