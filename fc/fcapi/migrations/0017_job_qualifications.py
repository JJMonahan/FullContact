# Generated by Django 4.2.7 on 2023-11-27 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcapi', '0016_alter_job_compensation_alter_job_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='qualifications',
            field=models.CharField(choices=[('0', 'Unknown'), ('1', 'Comfortable'), ('2', 'Challenged'), ('3', 'Stretching')], default='0', max_length=50),
        ),
    ]
