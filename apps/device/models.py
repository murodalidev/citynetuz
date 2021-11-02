from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from apps.index.models import TRENDS
from citynet import settings


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = '1. Categories'

#    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Parent Category', null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Parent Category', 
                                        limit_choices_to={'is_active': True, 'parent_category__isnull': True},
                                        related_name='children', null=True, blank=True, )
    title = models.CharField(max_length=50, verbose_name=_('Category title'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


class Product(models.Model):

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = '2. Products'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    trend = models.IntegerField(choices=TRENDS, verbose_name=_('Trend'), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=_('product title'))
    price = models.CharField(max_length=20, verbose_name=_('Price'))
    old_price = models.CharField(max_length=20, verbose_name=_('Old price'), null=True, blank=True)
    main_content = RichTextField(verbose_name=_('Main Content'))
    secondary_content = RichTextField(verbose_name=_('Secondary Content'), null=True, blank=True)
    is_popular = models.BooleanField(default=False, verbose_name=_('Is popular'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.title


def get_upload_to(instance, filename):
    return 'products/%i/%s' % (instance.product.id, filename)


class ProductImage(models.Model):

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = '3. Product images'
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    image = models.FileField(upload_to=get_upload_to, verbose_name=_('Image'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return f'image of {self.product.title}'

    @property
    def get_img_url(self):
        if settings.DEBUG:
            return f"{settings.LOCAL_BASE_URL}{self.image.url}"
        else:
            return f"{settings.PROD_BASE_URL}{self.image.url}"


class Request(models.Model):

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = '4. Requests'

    full_name = models.CharField(max_length=50, verbose_name=_('First name'))
    email = models.EmailField(verbose_name=_('Email address'), null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name=_('Phone number'))
    message = models.TextField(verbose_name=_('Message'))
    is_viewed = models.BooleanField(default=False, verbose_name=_('Is viewed'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    def __str__(self):
        return f'{self.full_name} - {self.date_created.date()}'
