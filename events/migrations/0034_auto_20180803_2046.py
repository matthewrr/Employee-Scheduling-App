# Generated by Django 2.0.6 on 2018-08-03 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0033_auto_20180803_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='template',
        ),
        migrations.AddField(
            model_name='eventschedule',
            name='template',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.EventTemplate'),
        ),
    ]
