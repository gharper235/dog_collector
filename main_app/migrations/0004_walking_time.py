# Generated by Django 3.2 on 2021-04-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210417_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='walking',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
