# Generated by Django 2.1.7 on 2019-05-17 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_intensivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='intensivo',
            name='turn',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
