# Generated by Django 3.0.2 on 2020-02-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0009_person_pword'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='pword',
            field=models.CharField(default='', max_length=200),
        ),
    ]
