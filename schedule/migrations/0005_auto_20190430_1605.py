# Generated by Django 2.1.7 on 2019-04-30 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20190430_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to=settings.AUTH_USER_MODEL),
        ),
    ]
