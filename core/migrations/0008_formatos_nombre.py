# Generated by Django 3.2.8 on 2024-01-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_docs_fechareg'),
    ]

    operations = [
        migrations.AddField(
            model_name='formatos',
            name='nombre',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]
