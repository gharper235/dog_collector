# Generated by Django 3.2 on 2021-04-21 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210421_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='flavor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
