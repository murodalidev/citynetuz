# Generated by Django 3.2.6 on 2021-09-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0008_auto_20210922_1204'),
        ('index', '0004_auto_20210920_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': "1. News'"},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'verbose_name': 'Object', 'verbose_name_plural': '3. Objects'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Partner', 'verbose_name_plural': '2. Partners'},
        ),
        migrations.RemoveField(
            model_name='object',
            name='trend',
        ),
        migrations.AddField(
            model_name='news',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='Is popular'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='News title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='News title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='News title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='News title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='trend',
            field=models.IntegerField(choices=[(0, 'Internet'), (1, 'Camera'), (2, 'Telephony'), (3, 'IPTV'), (4, 'Device'), (5, 'Montage'), (6, 'Design'), (7, 'Development')], default=0, verbose_name='Trend'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Partner title'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='title_en',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Partner title'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='title_ru',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Partner title'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='title_uz',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Partner title'),
        ),
        migrations.DeleteModel(
            name='Trend',
        ),
    ]