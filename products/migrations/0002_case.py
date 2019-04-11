# Generated by Django 2.1.7 on 2019-04-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, default=None, max_length=70, null=True)),
                ('product_type', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('brand', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('form_factor', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('built_in_powersupply', models.BooleanField()),
                ('power', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('audio_in_out', models.BooleanField()),
                ('usb_2_front', models.IntegerField(blank=True, default=None, max_length=2, null=True)),
                ('usb_3_front', models.IntegerField(blank=True, default=None, max_length=2, null=True)),
                ('graphic_adapter_size', models.IntegerField(blank=True, default=None, max_length=2, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Жесткий диск',
                'verbose_name_plural': 'Жесткие диски',
            },
        ),
    ]
