# Generated by Django 2.0.6 on 2018-08-14 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_schedule_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='event',
        ),
    ]