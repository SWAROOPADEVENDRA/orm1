# Generated by Django 5.0.3 on 2024-04-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='email',
            field=models.EmailField(default='haiall@gmail.com', max_length=254),
        ),
    ]