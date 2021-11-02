from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Product, ProductImage, Request


class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'parent_category', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active')
    autocomplete_fields = ('parent_category', )
    search_fields = ('title', )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(TranslationAdmin):
    inlines = (ProductImageInline, )
    list_display = ('id', 'category', 'title', 'trend', 'is_popular', 'is_active', 'date_created')
    fields = ('category', ('title', 'price', 'old_price'), ('trend', 'is_popular', 'is_active'),
              ('main_content', 'secondary_content'), 'date_created')
    readonly_fields = ('date_created', )
    list_filter = ('date_created', 'is_popular',  'is_active', 'trend', 'category')
    autocomplete_fields = ('category', )
    search_fields = ('title', )
    date_hierarchy = 'date_created'


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'is_active', 'date_created')
    list_filter = ('date_created', 'is_active', 'product')
    autocomplete_fields = ('product', )
    search_fields = ('product__title', )


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'is_viewed', 'date_created')
    list_filter = ('date_created', 'is_viewed')
    search_fields = ('title', 'full_name', 'email', 'phone')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Request, RequestAdmin)