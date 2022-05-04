# Generated by Django 3.2.8 on 2022-04-06 12:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20220405_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatepass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_no', models.CharField(max_length=15)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('applied_date', models.DateField()),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('place', models.CharField(max_length=101)),
                ('reason_for_leave', models.TextField(max_length=1001)),
                ('parents_name', models.CharField(max_length=101)),
                ('parents_pno', models.CharField(max_length=15)),
                ('parents_permission', models.BooleanField(default=False)),
                ('Year coordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('counsellor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Counsellor', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
