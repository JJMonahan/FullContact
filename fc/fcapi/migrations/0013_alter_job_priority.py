# Generated by Django 4.2.7 on 2023-11-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcapi', '0012_alter_job_location_alter_job_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='priority',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='Unknown', max_length=50),
        ),
    ]
