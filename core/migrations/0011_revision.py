# Generated by Django 3.2.8 on 2024-01-12 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='revision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obs', models.CharField(max_length=500)),
                ('estado', models.IntegerField()),
                ('archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formatos')),
                ('revisado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
