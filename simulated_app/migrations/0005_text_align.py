# Generated by Django 3.2.2 on 2021-06-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulated_app', '0004_auto_20210523_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='align',
            field=models.CharField(choices=[('text-start', 'Do lewej'), ('text-center', 'Środek'), ('text-end', 'Do prawej')], default='text-start', max_length=25),
        ),
    ]
