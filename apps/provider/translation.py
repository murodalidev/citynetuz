from modeltranslation.translator import translator, TranslationOptions
from .models import Notification, CityArea, DistrictArea, StreetArea, TypeChannel, Channel


class NotificationTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class CityAreaTranslationOptions(TranslationOptions):
    fields = ('title', )


class DistrictAreaTranslationOptions(TranslationOptions):
    fields = ('title', )


class StreetAreaTranslationOptions(TranslationOptions):
    fields = ('title', )


class TypeChannelTranslationOptions(TranslationOptions):
    fields = ('title', )


class ChannelTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(Notification, NotificationTranslationOptions)
translator.register(CityArea, CityAreaTranslationOptions)
translator.register(DistrictArea, DistrictAreaTranslationOptions)
translator.register(StreetArea, StreetAreaTranslationOptions)
translator.register(TypeChannel, TypeChannelTranslationOptions)
translator.register(Channel, ChannelTranslationOptions)
