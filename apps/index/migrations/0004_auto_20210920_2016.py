# Generated by Django 3.2.6 on 2021-09-20 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20210920_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Trend title'),
        ),
        migrations.AlterField(
            model_name='trend',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Trend title'),
        ),
        migrations.AlterField(
            model_name='trend',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Trend title'),
        ),
        migrations.AlterField(
            model_name='trend',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='Trend title'),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='objects', verbose_name='Image')),
                ('title', models.CharField(max_length=50, verbose_name='Partner title')),
                ('title_en', models.CharField(max_length=50, null=True, verbose_name='Partner title')),
                ('title_ru', models.CharField(max_length=50, null=True, verbose_name='Partner title')),
                ('title_uz', models.CharField(max_length=50, null=True, verbose_name='Partner title')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('trend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.trend', verbose_name='Trends')),
            ],
            options={
                'verbose_name': 'Object',
                'verbose_name_plural': '4. Objects',
            },
        ),
    ]
