# Generated by Django 2.0.6 on 2018-09-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0022_auto_20180830_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Location ID'),
        ),
        migrations.AlterField(
            model_name='position',
            name='code',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='position',
            name='short_name',
            field=models.CharField(max_length=8),
        ),
    ]