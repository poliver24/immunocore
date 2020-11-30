# Generated by Django 3.1.3 on 2020-11-30 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immunocore_app', '0005_auto_20201130_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='sequence',
            field=models.CharField(max_length=10000, validators=[django.core.validators.RegexValidator('^[ATCG]*$', 'Gene sequence can only contain characters A, T, C, or G')]),
        ),
    ]
