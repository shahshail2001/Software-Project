# Generated by Django 3.1.5 on 2021-03-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_login', '0004_auto_20210309_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_dob',
            field=models.DateField(),
        ),
    ]
