# Generated by Django 3.2.8 on 2022-04-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20220406_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_warden',
            field=models.BooleanField(default=False, help_text='If warden check this', verbose_name='Warden'),
        ),
    ]