# Generated by Django 3.1.6 on 2021-02-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210216_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tax_type',
            field=models.CharField(blank=True, choices=[('EST', 'Estandar'), ('NIP', 'No imponible'), ('PDG', 'Producto digital')], max_length=200, null=True),
        ),
    ]