# Generated by Django 4.0.3 on 2022-04-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, default='MaxMata', max_length=200, null=True),
        ),
    ]