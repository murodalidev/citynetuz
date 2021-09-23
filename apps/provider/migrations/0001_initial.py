# Generated by Django 3.2.6 on 2021-09-18 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CableTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Cable Technology name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'Cable Technology',
                'verbose_name_plural': 'Cable Technologies',
            },
        ),
        migrations.CreateModel(
            name='CityArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='City name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'City Area',
                'verbose_name_plural': 'City Areas',
            },
        ),
        migrations.CreateModel(
            name='DistrictArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='District name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.cityarea', verbose_name='City')),
            ],
            options={
                'verbose_name': 'District Area',
                'verbose_name_plural': 'District Areas',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Notification title')),
                ('content', models.TextField(verbose_name='Content')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Service title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tariff title')),
                ('global_speed', models.CharField(max_length=50, verbose_name='Global provider speed')),
                ('tasix_speed', models.CharField(max_length=50, verbose_name='Tas Ix speed')),
                ('price', models.CharField(max_length=20, verbose_name='Monthly price')),
                ('price_cash6', models.CharField(max_length=20, verbose_name='Monthly price for 6 months')),
                ('price_cash12', models.CharField(max_length=20, verbose_name='Monthly price for 12 months')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.service', verbose_name='Service')),
            ],
            options={
                'verbose_name': 'Tariff',
                'verbose_name_plural': 'Tariffs',
            },
        ),
        migrations.CreateModel(
            name='StreetArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Street name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.districtarea', verbose_name='District')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.cabletech', verbose_name='Cable Technology')),
            ],
            options={
                'verbose_name': 'Street Area',
                'verbose_name_plural': 'Street Areas',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porch', models.IntegerField(blank=True, max_length=2, null=True, verbose_name='Porch name')),
                ('flat', models.IntegerField(blank=True, max_length=3, null=True, verbose_name='Flat name')),
                ('full_name', models.CharField(max_length=50, verbose_name='Full name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone number')),
                ('is_viewed', models.BooleanField(default=False, verbose_name='Is viewed')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.cityarea', verbose_name='City')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.districtarea', verbose_name='District')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.streetarea', verbose_name='Street')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='HomeArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Street name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.streetarea', verbose_name='Street')),
            ],
            options={
                'verbose_name': 'Home Area',
                'verbose_name_plural': 'Home Areas',
            },
        ),
    ]
