# Generated by Django 2.0.6 on 2018-08-22 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0040_remove_event_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
