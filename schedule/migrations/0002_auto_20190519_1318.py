# Generated by Django 2.1.7 on 2019-05-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='suburb',
            field=models.CharField(max_length=100),
        ),
    ]
