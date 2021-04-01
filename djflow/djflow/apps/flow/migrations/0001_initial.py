# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 16:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descripción')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación')),
                ('is_active', models.BooleanField(default=True, help_text='¿Se puede utilizar esta cuenta o está inactiva?')),
                ('created_by', models.ForeignKey(help_text='Usuario que ha creado la cuenta', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Cuentas',
                'verbose_name': 'Cuenta',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('type', models.IntegerField(choices=[(0, 'Egreso'), (1, 'Ingreso')], default=1)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Categorías',
                'verbose_name': 'Categoría',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Descripción')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Monto')),
                ('date', models.DateField(help_text='Fecha del movimiento', verbose_name='Fecha')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(help_text='Cuenta a afectar', on_delete=django.db.models.deletion.CASCADE, to='flow.Account', verbose_name='Cuenta')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flow.Category', verbose_name='Categoría')),
                ('created_by', models.ForeignKey(help_text='Usuario que ha creado la cuenta', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name_plural': 'Transacciones',
                'verbose_name': 'Transacción',
            },
        ),
        migrations.CreateModel(
            name='TransactionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1200, verbose_name='Comentario')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flow.Transaction', verbose_name='Transacción')),
            ],
            options={
                'ordering': ('-timestamp',),
                'verbose_name_plural': 'Comentarios de transacciones',
                'verbose_name': 'Comentario de la transacción',
            },
        ),
    ]
