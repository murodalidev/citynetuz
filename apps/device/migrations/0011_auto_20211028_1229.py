# Generated by Django 3.2.6 on 2021-10-28 07:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0010_auto_20211028_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_content',
            field=ckeditor.fields.RichTextField(verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_content_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_content_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Secondary Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Secondary Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_content_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Secondary Content'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_content_uz',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Secondary Content'),
        ),
    ]
