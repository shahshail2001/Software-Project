# Generated by Django 3.1.5 on 2021-02-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
