# Generated by Django 2.0.6 on 2018-07-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.CharField(max_length=256),
        ),
    ]
