# Generated by Django 3.1.5 on 2021-02-27 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_order'),
        ('Operator', '0002_defectiveness_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='defectiveness_report',
            name='operator_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User.account_account'),
        ),
    ]
