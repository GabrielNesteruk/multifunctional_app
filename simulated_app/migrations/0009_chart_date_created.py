# Generated by Django 3.2.2 on 2021-06-13 22:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simulated_app', '0008_auto_20210613_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
