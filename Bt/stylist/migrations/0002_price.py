# Generated by Django 2.1.2 on 2018-11-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_session', models.CharField(max_length=250)),
                ('evening_session', models.CharField(max_length=250)),
                ('morning_session', models.CharField(max_length=250)),
            ],
        ),
    ]