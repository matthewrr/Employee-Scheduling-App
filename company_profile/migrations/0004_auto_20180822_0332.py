# Generated by Django 2.0.6 on 2018-08-22 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0003_remove_companyprofilerole_company_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
