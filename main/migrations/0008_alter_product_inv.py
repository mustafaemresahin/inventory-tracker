# Generated by Django 4.0.4 on 2022-11-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_inv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inv',
            field=models.CharField(max_length=100),
        ),
    ]
