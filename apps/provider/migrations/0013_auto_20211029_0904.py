# Generated by Django 3.2.6 on 2021-10-29 04:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0012_alter_request_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='content_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Content'),
        ),
    ]
