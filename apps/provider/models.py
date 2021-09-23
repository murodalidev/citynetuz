from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = '1. Notifications'

    title = models.CharField(max_length=50, verbose_name=_('Notification title'))
    content = models.TextField(verbose_name=_('Content'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class InternetTariff(models.Model):

    class Meta:
        verbose_name = 'Internet tariff'
        verbose_name_plural = '2. Internet tariffs'

    title = models.CharField(max_length=50, verbose_name=_('Tariff title'))
    speed = models.CharField(max_length=50, verbose_name=_('Internet speed'))
    tas_ix = models.CharField(max_length=50, verbose_name=_('Tas Ix speed'), null=True, blank=True)
    price = models.CharField(max_length=20, verbose_name=_('Monthly price'))
    price_cash6 = models.CharField(max_length=20, verbose_name=_('Monthly price for 6 months'), null=True, blank=True)
    price_cash12 = models.CharField(max_length=20, verbose_name=_('Monthly price for 12 months'), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class TelephonyTariff(models.Model):

    class Meta:
        verbose_name = 'Telephony tariff'
        verbose_name_plural = '3. Telephony tariffs'

    title = models.CharField(max_length=50, verbose_name=_('Tariff title'))
    minutes = models.CharField(max_length=50, verbose_name=_('Minutes'))
    price = models.CharField(max_length=20, verbose_name=_('Monthly price'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class CityArea(models.Model):

    class Meta:
        verbose_name = 'City Area'
        verbose_name_plural = '4. City Areas'

    title = models.CharField(max_length=50, verbose_name=_('City name'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class DistrictArea(models.Model):

    class Meta:
        verbose_name = 'District Area'
        verbose_name_plural = '4.1. District Areas'

    city = models.ForeignKey(CityArea, on_delete=models.CASCADE, verbose_name=_('City'))
    title = models.CharField(max_length=50, verbose_name=_('District name'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class CableTech(models.Model):

    class Meta:
        verbose_name = 'Cable Technology'
        verbose_name_plural = '4.2. Cable Technologies'

    title = models.CharField(max_length=50, verbose_name=_('Cable Technology name'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class StreetArea(models.Model):

    class Meta:
        verbose_name = 'Street Area'
        verbose_name_plural = '4.3. Street Areas'

    district = models.ForeignKey(DistrictArea, on_delete=models.CASCADE, verbose_name=_('District'))
    title = models.CharField(max_length=50, verbose_name=_('Street name'))
    tech = models.ForeignKey(CableTech, on_delete=models.CASCADE, verbose_name=_('Cable Technology'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class HomeArea(models.Model):

    class Meta:
        verbose_name = 'Home Area'
        verbose_name_plural = '4.4. Home Areas'

    street = models.ForeignKey(StreetArea, on_delete=models.CASCADE, verbose_name=_('Street'))
    title = models.CharField(max_length=50, verbose_name=_('Home name'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class Request(models.Model):

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = '5. Requests'

    city = models.ForeignKey(CityArea, on_delete=models.CASCADE, verbose_name=_('City'))
    district = models.ForeignKey(DistrictArea, on_delete=models.CASCADE, verbose_name=_('District'))
    street = models.ForeignKey(StreetArea, on_delete=models.CASCADE, verbose_name=_('Street'))
    home = models.ForeignKey(HomeArea, on_delete=models.CASCADE, verbose_name=_('Home'))
    flat = models.IntegerField(verbose_name=_('Flat name'), null=True, blank=True)
    full_name = models.CharField(max_length=50, verbose_name=_('Full name'))
    phone = models.CharField(max_length=50, verbose_name=_('Phone number'))
    is_viewed = models.BooleanField(default=False, verbose_name=_('Is viewed'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.full_name


class TypeChannel(models.Model):

    class Meta:
        verbose_name = 'Type Channel'
        verbose_name_plural = '6. Type Channels'

    title = models.CharField(max_length=50, verbose_name=_('Title'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class Channel(models.Model):

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = '6.1. Channels'

    type_channel = models.ForeignKey(TypeChannel, on_delete=models.CASCADE, verbose_name=_('Type channel'),
                                     related_name='channels')
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    image = models.ImageField(upload_to='channels', verbose_name=_('Channel image'))
    is_popular = models.BooleanField(default=False, verbose_name=_('Is popular'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title
