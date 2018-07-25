# Generated by Django 2.0.6 on 2018-07-23 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_schedule_employees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='schedule_name',
        ),
        migrations.AddField(
            model_name='schedule',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]