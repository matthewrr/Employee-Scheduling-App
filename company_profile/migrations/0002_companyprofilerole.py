# Generated by Django 2.0.6 on 2018-08-15 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfileRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verbose_name', models.CharField(blank=True, max_length=256, null=True)),
                ('short_name', models.CharField(blank=True, max_length=256, null=True)),
                ('company_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company_profile.CompanyProfile')),
            ],
        ),
    ]