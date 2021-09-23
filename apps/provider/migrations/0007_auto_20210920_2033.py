# Generated by Django 3.2.6 on 2021-09-20 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0006_camera_channel_typechannel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cabletech',
            options={'verbose_name': 'Cable Technology', 'verbose_name_plural': '3.2. Cable Technologies'},
        ),
        migrations.AlterModelOptions(
            name='camera',
            options={'verbose_name': 'Camera', 'verbose_name_plural': '6. Cameras'},
        ),
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': 'Channel', 'verbose_name_plural': '5.1. Channels'},
        ),
        migrations.AlterModelOptions(
            name='districtarea',
            options={'verbose_name': 'District Area', 'verbose_name_plural': '3.1. District Areas'},
        ),
        migrations.AlterModelOptions(
            name='homearea',
            options={'verbose_name': 'Home Area', 'verbose_name_plural': '3.4. Home Areas'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Request', 'verbose_name_plural': '4. Requests'},
        ),
        migrations.AlterModelOptions(
            name='streetarea',
            options={'verbose_name': 'Street Area', 'verbose_name_plural': '3.3. Street Areas'},
        ),
        migrations.AlterModelOptions(
            name='typechannel',
            options={'verbose_name': 'Type Channel', 'verbose_name_plural': '5. Type Channels'},
        ),
    ]
