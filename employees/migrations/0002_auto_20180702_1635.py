# Generated by Django 2.0.6 on 2018-07-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default='', max_length=8),
        ),
    ]
