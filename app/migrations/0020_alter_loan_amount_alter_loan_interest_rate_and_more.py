# Generated by Django 4.1.1 on 2022-09-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_loan_compound_interest_alter_loan_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='amount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='loan',
            name='num_times_interest',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='loan',
            name='time_period',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
