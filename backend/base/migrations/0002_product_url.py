# Generated by Django 4.0.3 on 2022-04-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]