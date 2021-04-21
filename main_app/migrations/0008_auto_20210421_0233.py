# Generated by Django 3.2 on 2021-04-21 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_dog_foods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='color',
        ),
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='food',
            field=models.CharField(choices=[('0', 'N/A'), ('1', 'Treat'), ('2', 'Meal')], default='0', max_length=1),
        ),
    ]