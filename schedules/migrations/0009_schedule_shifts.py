# Generated by Django 2.0.6 on 2018-08-22 21:50

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_schedule_active_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='shifts',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
