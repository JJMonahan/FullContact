# Generated by Django 4.2.6 on 2023-11-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='role',
            field=models.IntegerField(),
        ),
    ]
