# Generated by Django 3.0.7 on 2020-06-21 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('probability', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('wind_degree', models.IntegerField(default=0)),
                ('probability', models.FloatField(default=0.0)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hours', to='planes.Day')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
