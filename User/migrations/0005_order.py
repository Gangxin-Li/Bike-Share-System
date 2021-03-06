# Generated by Django 3.1.5 on 2021-02-21 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Operator', '0002_defectiveness_report'),
        ('User', '0004_auto_20210221_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('checkout_time', models.TimeField()),
                ('due_amount', models.FloatField()),
                ('is_complete', models.BooleanField()),
                ('fix_amount', models.FloatField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Operator.bike')),
                ('end', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_station', to='Operator.station')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_station', to='Operator.station')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.account_account')),
            ],
            options={
                'db_table': 'User_order',
            },
        ),
    ]
