# Generated by Django 4.2.11 on 2024-05-29 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitgo', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='address',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='bitgo.address'),
            preserve_default=False,
        ),
    ]
