from modeltranslation.translator import translator, TranslationOptions
from .models import News, Partner, Object


class NewsTranslatorAdmin(TranslationOptions):
    fields = ('title', 'content')


class PartnerTranslatorAdmin(TranslationOptions):
    fields = ('title', )


class ObjectTranslatorAdmin(TranslationOptions):
    fields = ('title', )


translator.register(News, NewsTranslatorAdmin)
translator.register(Partner, PartnerTranslatorAdmin)
translator.register(Object, ObjectTranslatorAdmin)
