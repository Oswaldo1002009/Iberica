# Generated by Django 2.1.7 on 2019-04-24 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolled',
            name='level',
        ),
    ]
