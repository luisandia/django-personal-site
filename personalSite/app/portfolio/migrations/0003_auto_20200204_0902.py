# Generated by Django 3.0.2 on 2020-02-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190716_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion web'),
        ),
    ]
