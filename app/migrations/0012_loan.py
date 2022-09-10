# Generated by Django 4.1.1 on 2022-09-09 09:18

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.FloatField(default=7000, validators=[app.models.validate_principal])),
                ('interest', models.FloatField(default=0)),
                ('months', models.IntegerField(default=0)),
                ('payable_amount', models.FloatField(default=0, validators=[app.models.calculate_interest])),
                ('status', models.CharField(default=0, max_length=12)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('creditofficer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.creditofficer')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Applicant', to='app.customer')),
            ],
        ),
    ]
