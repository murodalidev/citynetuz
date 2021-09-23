# Generated by Django 3.2.6 on 2021-09-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20210920_1802'),
        ('provider', '0002_auto_20210920_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cabletech',
            options={'verbose_name': 'Cable Technology', 'verbose_name_plural': '5. Cable Technologies'},
        ),
        migrations.AlterModelOptions(
            name='cityarea',
            options={'verbose_name': 'City Area', 'verbose_name_plural': '3. City Areas'},
        ),
        migrations.AlterModelOptions(
            name='districtarea',
            options={'verbose_name': 'District Area', 'verbose_name_plural': '4. District Areas'},
        ),
        migrations.AlterModelOptions(
            name='homearea',
            options={'verbose_name': 'Home Area', 'verbose_name_plural': '7. Home Areas'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Notification', 'verbose_name_plural': '1. Notifications'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Request', 'verbose_name_plural': '8. Requests'},
        ),
        migrations.AlterModelOptions(
            name='streetarea',
            options={'verbose_name': 'Street Area', 'verbose_name_plural': '6. Street Areas'},
        ),
        migrations.AlterModelOptions(
            name='tariff',
            options={'verbose_name': 'Tariff', 'verbose_name_plural': '2. Tariffs'},
        ),
        migrations.AddField(
            model_name='notification',
            name='trend',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='index.trend', verbose_name='Trend'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tariff',
            name='trend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.trend', verbose_name='Trend'),
        ),
    ]