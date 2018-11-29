# Generated by Django 2.1.2 on 2018-11-28 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancer_name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('value', models.IntegerField()),
                ('type', models.CharField(choices=[('Stylist', 'Stylist'), ('Educator', 'Educator')], default='Stylist', max_length=250)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('FREE', 'free'), ('BUSY', 'busy')], default='FREE', max_length=250)),
                ('evening', models.CharField(choices=[('FREE', 'free'), ('BUSY', 'busy')], default='FREE', max_length=250)),
                ('morning', models.CharField(choices=[('FREE', 'free'), ('BUSY', 'busy')], default='FREE', max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='freelancer',
            name='time_slot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stylist.Timeslot'),
        ),
    ]
