# Generated by Django 3.2.6 on 2021-09-20 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_trend_parent_trend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': "2. News'"},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Partner', 'verbose_name_plural': '3. Partners'},
        ),
        migrations.AlterModelOptions(
            name='trend',
            options={'verbose_name': 'Trend', 'verbose_name_plural': '1. Trends'},
        ),
    ]