# Generated by Django 4.1.1 on 2022-09-12 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
    ]
