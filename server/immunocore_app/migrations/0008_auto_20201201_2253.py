# Generated by Django 3.1.3 on 2020-12-01 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immunocore_app', '0007_auto_20201130_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='sequence',
            field=models.CharField(max_length=10000, unique=True, validators=[django.core.validators.RegexValidator('^[ATCG]*$', 'Gene sequence can only contain characters A, T, C, or G')]),
        ),
        migrations.AlterField(
            model_name='protein',
            name='sequence',
            field=models.CharField(max_length=10000, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]*$', 'Protein sequence can only contain letters A-Z')]),
        ),
    ]
