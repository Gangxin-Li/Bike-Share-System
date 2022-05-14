# Generated by Django 3.1.5 on 2021-02-12 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(default='', max_length=100)),
                ('station_latitude', models.FloatField(null=True)),
                ('station_longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_use', models.BooleanField(default=False)),
                ('is_faulty', models.BooleanField(default=False)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operator.station')),
            ],
            options={
                'verbose_name_plural': 'Bikes',
            },
        ),
    ]
