# Generated by Django 2.0.6 on 2018-08-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0018_position_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationcategory',
            name='color',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
