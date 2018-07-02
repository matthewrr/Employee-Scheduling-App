from django.db import migrations, models

class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name="employees_employee",
            fields=['first_name', models.CharField(default='', max_length=64)]
            )
    ] 