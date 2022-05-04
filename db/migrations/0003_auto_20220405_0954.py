# Generated by Django 3.2.8 on 2022-04-05 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_user_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='To block the user uncheck this', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_counsellor',
            field=models.BooleanField(default=False, help_text='If Counsellor check this', verbose_name='Counsellor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_hod',
            field=models.BooleanField(default=False, help_text='If HOD check this', verbose_name='HOD'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='If principal Check this', verbose_name='Principal status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=True, help_text='If student check this', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Check this if the user is super user(Super user has the highest privilages)', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_year_coordinator',
            field=models.BooleanField(default=False, help_text='If year coordinator check this', verbose_name='Year Coordinator'),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
