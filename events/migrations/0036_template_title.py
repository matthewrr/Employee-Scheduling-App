# Generated by Django 2.0.6 on 2018-08-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0035_template_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
    ]
