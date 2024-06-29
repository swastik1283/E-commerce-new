# Generated by Django 4.2.7 on 2024-02-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_title', models.CharField(max_length=50)),
                ('prod_price', models.FloatField()),
                ('prod_discount', models.FloatField()),
                ('prod_disc', models.TextField()),
                ('prod_comp', models.CharField(max_length=50)),
                ('prod_art', models.CharField(max_length=50)),
                ('prod_cata', models.CharField(choices=[('sr', 'shirt'), ('pn', 'pant'), ('ct', 'coat'), ('lw', 'lower'), ('ts', 'tshirt'), ('hs', 'hosiery')], max_length=2)),
                ('prod_img', models.ImageField(upload_to='products')),
            ],
        ),
    ]
