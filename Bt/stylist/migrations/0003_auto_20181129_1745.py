# Generated by Django 2.1.2 on 2018-11-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylist', '0002_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
