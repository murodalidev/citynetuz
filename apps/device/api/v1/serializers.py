from rest_framework import serializers
from ...models import Category, Product, ProductImage, Request


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        qs = Category.objects.filter(parent_category=obj, is_active=True)
        sz = SubCategorySerializer(qs, many=True)
        return sz.data

    class Meta:
        model = Category
        fields = ('id', 'title', 'children')


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('id', 'get_img_url')


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        qs = ProductImage.objects.filter(is_active=True, product=obj)
        sz = ProductImageSerializer(instance=qs, many=True)
        return sz.data

    class Meta:
        model = Product
        fields = ('id', 'category', 'category_name', 'title', 'images', 'price', 'old_price', 'main_content',
                  'secondary_content')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('full_name', 'email', 'phone', 'message')
