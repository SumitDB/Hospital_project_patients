# Generated by Django 4.0.6 on 2022-08-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0013_alter_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='temprature',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1, null=True),
        ),
    ]