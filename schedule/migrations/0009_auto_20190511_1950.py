# Generated by Django 2.1.7 on 2019-05-12 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20190507_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
