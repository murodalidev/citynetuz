from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, Partner, Object


class NewsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'trend', 'is_popular', 'is_active', 'date_created')
    fields = ('title', 'image', ('trend', 'is_popular', 'is_active'), 'content', 'date_created')
    readonly_fields = ('date_created', )
    list_filter = ('date_created', 'is_popular', 'is_active', 'trend')
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class PartnerAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )


class ObjectAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Object, ObjectAdmin)
