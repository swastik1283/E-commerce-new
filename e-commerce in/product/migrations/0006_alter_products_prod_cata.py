# Generated by Django 4.2.7 on 2024-02-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_products_prod_disc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prod_cata',
            field=models.CharField(choices=[('sr', 'shirt'), ('pn', 'pant'), ('ct', 'coat'), ('lw', 'lower'), ('ts', 'tshirt'), ('kt', 'kurta'), ('hs', 'hosiery')], max_length=2),
        ),
    ]
