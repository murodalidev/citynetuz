from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Product


class CategoryTranslatorAdmin(TranslationOptions):
    fields = ('title', )


class ProductTranslatorAdmin(TranslationOptions):
    fields = ('title', 'main_content', 'secondary_content')


translator.register(Category, CategoryTranslatorAdmin)
translator.register(Product, ProductTranslatorAdmin)
