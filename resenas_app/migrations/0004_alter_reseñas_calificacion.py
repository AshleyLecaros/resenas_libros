# Generated by Django 4.2.11 on 2024-05-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenas_app', '0003_alter_usuarios_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseñas',
            name='calificacion',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
