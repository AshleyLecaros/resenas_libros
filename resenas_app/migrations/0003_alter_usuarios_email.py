# Generated by Django 4.2.11 on 2024-05-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenas_app', '0002_usuarios_email_alter_usuarios_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(default='', max_length=50, unique=True),
        ),
    ]
