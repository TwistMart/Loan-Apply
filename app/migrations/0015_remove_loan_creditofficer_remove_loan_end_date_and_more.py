# Generated by Django 4.1.1 on 2022-09-12 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_loan_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='creditofficer',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='months',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='start_date',
        ),
    ]
