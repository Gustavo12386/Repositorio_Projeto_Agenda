# Generated by Django 4.0.4 on 2022-04-26 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_mostrar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='mostrar',
        ),
    ]
