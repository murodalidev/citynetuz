from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Notification, InternetTariff, CityArea, DistrictArea, CableTech, StreetArea, HomeArea, Request, \
    TypeChannel, Channel, TelephonyTariff


class NotificationAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class InternetTariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'speed', 'tas_ix', 'price', 'price_cash6', 'price_cash12', 'is_active',
                    'date_created')
    fields = ('title', ('speed', 'tas_ix'), ('price', 'price_cash6', 'price_cash12'), 'is_active', 'date_created')
    readonly_fields = ('date_created', )
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class TelephonyTariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'minutes', 'price',  'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class CityAreaAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class DistrictAreaAdmin(TranslationAdmin):
    list_display = ('id', 'city', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    autocomplete_fields = ('city', )
    date_hierarchy = 'date_created'


class CableTechAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class StreetAreaAdmin(TranslationAdmin):
    list_display = ('id', 'district', 'title', 'tech', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active', 'tech')
    search_fields = ('title', )
    autocomplete_fields = ('district', )
    date_hierarchy = 'date_created'


class HomeAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    autocomplete_fields = ('street', )
    date_hierarchy = 'date_created'


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'city', 'district', 'street', 'flat', 'is_viewed', 'date_created')
    list_filter = ('date_created', 'is_viewed')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class TypeChannelAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class ChannelAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'type_channel', 'is_popular', 'is_active', 'date_created')
    fields = ('type_channel', 'title', 'image', ('is_popular', 'is_active'), 'date_created')
    readonly_fields = ('date_created', )
    list_filter = ('date_created', 'is_popular', 'is_active', 'type_channel')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


admin.site.register(Notification, NotificationAdmin)
admin.site.register(InternetTariff, InternetTariffAdmin)
admin.site.register(TelephonyTariff, TelephonyTariffAdmin)
admin.site.register(CityArea, CityAreaAdmin)
admin.site.register(DistrictArea, DistrictAreaAdmin)
admin.site.register(CableTech, CableTechAdmin)
admin.site.register(StreetArea, StreetAreaAdmin)
admin.site.register(HomeArea, HomeAreaAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(TypeChannel, TypeChannelAdmin)
admin.site.register(Channel, ChannelAdmin)
