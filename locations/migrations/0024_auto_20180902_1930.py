# Generated by Django 2.0.6 on 2018-09-02 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0023_auto_20180901_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.LocationCategory'),
        ),
    ]
