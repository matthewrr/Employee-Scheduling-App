# Generated by Django 2.0.6 on 2018-07-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]