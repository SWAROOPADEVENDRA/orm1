# Generated by Django 5.0.3 on 2024-04-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_webpage_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='date_and_time',
            field=models.DateTimeField(default='today'),
        ),
    ]
