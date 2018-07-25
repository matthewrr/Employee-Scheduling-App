# Generated by Django 2.0.6 on 2018-07-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0031_auto_20180725_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventlocation',
            options={'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='eventschedule',
            options={'verbose_name_plural': 'Schedule'},
        ),
        migrations.AlterField(
            model_name='event',
            name='doors_open',
            field=models.CharField(max_length=256, verbose_name='Doors Open'),
        ),
    ]