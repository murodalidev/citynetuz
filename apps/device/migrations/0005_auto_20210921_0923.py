# Generated by Django 3.2.6 on 2021-09-21 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_auto_20210921_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='product title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='product title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='product title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='product title'),
        ),
    ]
