# Generated by Django 3.0.2 on 2020-02-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0003_companytable'),
    ]

    operations = [
        migrations.CreateModel(
            name='akash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comname', models.CharField(max_length=200)),
                ('drname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('Dateesbh', models.CharField(max_length=200)),
                ('mobilenumber', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('regidno', models.CharField(max_length=200)),
                ('pic', models.CharField(max_length=200)),
                ('licensenumber', models.CharField(max_length=200)),
                ('gstnumber', models.CharField(max_length=200)),
                ('pword', models.CharField(max_length=200)),
                ('vnumber', models.CharField(max_length=200)),
            ],
        ),
    ]
