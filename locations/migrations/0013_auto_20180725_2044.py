# Generated by Django 2.0.6 on 2018-07-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0012_auto_20180722_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
