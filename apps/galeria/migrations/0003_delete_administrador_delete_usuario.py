# Generated by Django 5.0.4 on 2024-07-16 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_alter_tabelanutricional_usuarioreferencia'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
