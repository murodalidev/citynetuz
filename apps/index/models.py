from django.db import models
from django.utils.translation import gettext_lazy as _


TRENDS = (
    (0, 'Internet'),
    (1, 'Telephony'),
    (2, 'IPTV'),
    (3, 'Camera'),
    (4, 'Device'),
    (5, 'Montage'),
    (6, 'Design'),
    (7, 'Development'),
)


class News(models.Model):

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = '1. News\''

    trend = models.IntegerField(choices=TRENDS, default=0, verbose_name=_('Trend'))
    image = models.FileField(upload_to='news', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('News title'))
    content = models.TextField(verbose_name=_('Content'))
    is_popular = models.BooleanField(default=False, verbose_name=_('Is popular'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class Partner(models.Model):

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = '2. Partners'

    image = models.FileField(upload_to='partner', verbose_name=_('Image'))
    title = models.CharField(max_length=50, verbose_name=_('Partner title'), null=True, blank=True)
    link = models.URLField(verbose_name=_('Partner link'), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class Object(models.Model):

    class Meta:
        verbose_name = 'Object'
        verbose_name_plural = '3. Objects'

    image = models.FileField(upload_to='objects', verbose_name=_('Image'))
    title = models.CharField(max_length=50, verbose_name=_('Partner title'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


