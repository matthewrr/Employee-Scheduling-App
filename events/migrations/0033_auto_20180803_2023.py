# Generated by Django 2.0.6 on 2018-08-03 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0032_auto_20180725_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='template',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shift',
            name='event_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventLocation', verbose_name='Event Location'),
        ),
    ]
