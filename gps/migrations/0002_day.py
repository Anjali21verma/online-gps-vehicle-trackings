# Generated by Django 3.0.2 on 2020-02-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fatherName', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('birthDate', models.CharField(max_length=200)),
                ('mobilenumber', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('idproof', models.CharField(max_length=200)),
                ('idno', models.CharField(max_length=200)),
                ('pic', models.CharField(max_length=200)),
            ],
        ),
    ]
