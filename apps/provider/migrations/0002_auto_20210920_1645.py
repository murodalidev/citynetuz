# Generated by Django 3.2.6 on 2021-09-20 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_trend_parent_trend'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariff',
            name='service',
        ),
        migrations.AddField(
            model_name='cityarea',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='City name'),
        ),
        migrations.AddField(
            model_name='cityarea',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='City name'),
        ),
        migrations.AddField(
            model_name='cityarea',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='City name'),
        ),
        migrations.AddField(
            model_name='districtarea',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='District name'),
        ),
        migrations.AddField(
            model_name='districtarea',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='District name'),
        ),
        migrations.AddField(
            model_name='districtarea',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='District name'),
        ),
        migrations.AddField(
            model_name='notification',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='notification',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='notification',
            name='content_uz',
            field=models.TextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='notification',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Notification title'),
        ),
        migrations.AddField(
            model_name='notification',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Notification title'),
        ),
        migrations.AddField(
            model_name='notification',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='Notification title'),
        ),
        migrations.AddField(
            model_name='streetarea',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Street name'),
        ),
        migrations.AddField(
            model_name='streetarea',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Street name'),
        ),
        migrations.AddField(
            model_name='streetarea',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='Street name'),
        ),
        migrations.AddField(
            model_name='tariff',
            name='trend',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.trend', verbose_name='Service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='flat',
            field=models.IntegerField(blank=True, null=True, verbose_name='Flat name'),
        ),
        migrations.AlterField(
            model_name='request',
            name='porch',
            field=models.IntegerField(blank=True, null=True, verbose_name='Porch name'),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]