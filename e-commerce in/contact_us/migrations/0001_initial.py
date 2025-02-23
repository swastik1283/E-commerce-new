# Generated by Django 4.2.7 on 2024-03-06 13:54

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('issue', models.CharField(max_length=50)),
                ('order_no', models.CharField(max_length=50)),
                ('message', tinymce.models.HTMLField()),
            ],
        ),
    ]
