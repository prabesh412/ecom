# Generated by Django 4.0.1 on 2022-01-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
