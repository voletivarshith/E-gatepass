# Generated by Django 3.2.8 on 2022-04-04 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
