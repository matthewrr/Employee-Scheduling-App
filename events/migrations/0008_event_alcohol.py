# Generated by Django 2.0.6 on 2018-07-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180705_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='alcohol',
            field=models.BooleanField(default=True),
        ),
    ]
