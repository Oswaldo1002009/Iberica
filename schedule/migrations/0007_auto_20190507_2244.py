# Generated by Django 2.1.7 on 2019-05-08 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20190507_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='enrolled',
            name='zip_code',
            field=models.CharField(max_length=5),
        ),
    ]
