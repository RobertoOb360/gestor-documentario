# Generated by Django 3.2.8 on 2024-01-06 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_activities_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='repositorio/formatos'),
        ),
        migrations.AlterField(
            model_name='formatos',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='usuarios/portafolio'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='solicitante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='voucher',
            field=models.FileField(blank=True, null=True, upload_to='usuarios/vouchers'),
        ),
    ]
