# Generated by Django 2.0.6 on 2018-08-19 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0040_remove_event_schedule'),
        ('schedules', '0004_remove_schedule_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='event',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]
