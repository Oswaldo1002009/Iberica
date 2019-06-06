# Generated by Django 2.1.7 on 2019-06-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20190605_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intensivo',
            name='i1m1',
            field=models.CharField(blank=True, choices=[('El Carpeta (Bulerías)', 'El Carpeta (Bulerías)'), ('Nazaret Reyes (Alegrías)', 'Nazaret Reyes (Alegrías)'), ('NIVEL AVANZADO - Rafael Estévez (Cantiña del amarano)', 'NIVEL AVANZADO - Rafael Estévez (Cantiña del amarano)'), ('NIVEL AVANZADO - Valeriano Paños (Martinete)', 'NIVEL AVANZADO - Valeriano Paños (Martinete)'), ('NIVEL PROFESIONAL - Javier LaTorre', 'NIVEL PROFESIONAL - Javier LaTorre')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i2m1',
            field=models.CharField(blank=True, choices=[('Eduardo Guerrero (Bulerías)', 'Eduardo Guerrero (Bulerías)'), ('El Carpeta (Seguiriyas)', 'El Carpeta (Seguiriyas)'), ('NIVEL AVANZADO - María Moreno (Bata de Cola por Alegrías)', 'NIVEL AVANZADO - María Moreno (Bata de Cola por Alegrías)'), ('NIVEL AVANZADO - Ana Morales (Seguiriya)', 'NIVEL AVANZADO - Ana Morales (Seguiriya)'), ('NIVEL PROFESIONAL - Pedro Córdoba', 'NIVEL PROFESIONAL - Pedro Córdoba')], max_length=150),
        ),
    ]
