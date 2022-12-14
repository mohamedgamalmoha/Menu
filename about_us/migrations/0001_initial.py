# Generated by Django 4.1.1 on 2022-10-12 19:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(verbose_name='Facebook link')),
                ('instagram', models.URLField(verbose_name='Instagram link')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Invalid Phone Number')], verbose_name='Whatsapp number')),
            ],
            options={
                'verbose_name': 'Website Main Info',
                'verbose_name_plural': 'Website Main Info',
            },
        ),
    ]
