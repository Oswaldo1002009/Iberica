# Generated by Django 2.1.7 on 2019-05-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20190507_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='disease',
            field=models.TextField(blank=True),
        ),
    ]
