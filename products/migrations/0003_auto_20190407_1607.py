# Generated by Django 2.1.7 on 2019-04-07 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_case'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'verbose_name': 'Корпус', 'verbose_name_plural': 'Корпуса для ПК'},
        ),
    ]